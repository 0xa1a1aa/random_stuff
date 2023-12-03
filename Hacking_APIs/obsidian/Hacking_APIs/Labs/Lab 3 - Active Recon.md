# Discover the host and enumerate the services

**Nmap scan**
```SHELL
nmap -v -n -p- -sV -sC 10.0.0.0/24
```

**Nmap result**
```
[...]
8888/tcp open http OpenResty web app server 1.17.8.2
|_http-title: crAPI
| http-methods:
|_ Supported Methods: GET HEAD
|_http-server-header: openresty/1.17.8.2
|_http-favicon: Unknown favicon MD5: 6E1267D9D946B0236CDF6FFD02890894
[...]
```

# Inspect JS files loaded by the web page
  
The JavaScript file **/static/js/main.e9428675.chunk.js** contains API endpoints. Search for "api" to find them.