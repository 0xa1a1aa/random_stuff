from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import sys
import re


def usage():
    print(f"sys.argv[0] <port> <upload-dir>")

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/upload':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
                <html>
                <body>
                    <h2>Upload File</h2>
                    <form enctype="multipart/form-data" method="post">
                        <input type="file" name="file" />
                        <input type="submit" value="Upload" />
                    </form>
                </body>
                </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/upload':
            content_type = self.headers['Content-Type']
            if not content_type.startswith('multipart/form-data'):
                self.send_error(400, "Bad Request: Content-Type not supported")
                return

            # Extract boundary from the content type
            boundary = content_type.split('=')[1].encode('utf-8')
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            # Split the body by the boundary
            parts = body.split(boundary)

            # Loop through parts to find the file data
            for part in parts:
                if b'Content-Disposition' in part and b'filename=' in part:
                    # Get the filename
                    header, file_data = part.split(b'\r\n\r\n', 1)
                    file_data = file_data.rsplit(b'\r\n--', 1)[0]  # Strip the trailing boundary

                    # Extract filename using regex for better accuracy
                    header_str = header.decode('utf-8')
                    filename_match = re.search(r'filename="(.+?)"', header_str)
                    if filename_match:
                        filename = filename_match.group(1)
                        filename = os.path.basename(filename)  # Prevent directory traversal
                    else:
                        filename = "unknown_file"

                    # Save the file
                    if not os.path.exists(UPLOAD_DIR):
                        os.makedirs(UPLOAD_DIR)
                    file_path = os.path.join(UPLOAD_DIR, filename)
                    with open(file_path, 'wb') as f:
                        f.write(file_data)

                    # Respond to the client
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f"File '{filename}' uploaded successfully!".encode('utf-8'))
                    return

            # If no file was found
            self.send_error(400, "No file uploaded or bad form data")
        else:
            self.send_error(404, "File not found")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        exit(1)
    PORT = int(sys.argv[1])
    UPLOAD_DIR = sys.argv[2]
    server = HTTPServer(('0.0.0.0', PORT), CustomHandler)
    print(f"Serving on port {PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
