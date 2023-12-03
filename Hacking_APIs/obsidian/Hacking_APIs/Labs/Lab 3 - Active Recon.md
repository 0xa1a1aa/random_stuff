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

**Identified endpoints:**
* LOGIN: api/auth/login
* GET_USER: api/v2/user/dashboard
* VERIFY_OTP: api/auth/v3/check-otp
* LOGIN_TOKEN: api/auth/v4.0/user/login-with-token
* ADD_VEHICLE: api/v2/vehicle/add_vehicle
* GET_VEHICLES: api/v2/vehicle/vehicles
* RESEND_MAIL: api/v2/vehicle/resend_email
* CHANGE_EMAIL: api/v2/user/change-email
* VERIFY_TOKEN: api/v2/user/verify-email-token
* UPLOAD_PROFILE_PIC: api/v2/user/pictures
* UPLOAD_VIDEO: api/v2/user/videos
* CHANGE_VIDEO_NAME: api/v2/user/videos/\<videoId>
* REFRESH_LOCATION: api/v2/vehicle/\<carId>/location
* CONVERT_VIDEO: api/v2/user/videos/convert_video
* CONTACT_MECHANIC: api/merchant/contact_mechanic
* RECEIVE_REPORT: api/mechanic/receive_report
* GET_MECHANICS: api/mechanic
* GET_PRODUCTS: api/shop/products
* GET_SERVICES: api/mechanic/service_requests
* BUY_PRODUCT: api/shop/orders"
* GET_ORDERS: api/shop/orders/all"
* GET_ORDER_BY_ID: api/shop/orders/\<orderId>
* RETURN_ORDER: api/shop/orders/return_order
* APPLY_COUPON: api/shop/apply_coupon
* ADD_NEW_POST: api/v2/community/posts
* GET_POSTS: api/v2/community/posts/recent
* GET_POST_BY_ID: api/v2/community/posts/\<postId>
* ADD_COMMENT: api/v2/community/posts/\<postId>/comment
* VALIDATE_COUPON: api/v2/coupon/validate-coupon

Search for "secrets" yields (doesnt look interesting):
* \_\_SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED
* SECRET_DO_NOT_PASS_THIS_OR_YOU_WILL_BE_FIRED
* SECRET_COMBOBOX_MODE_DO_NOT_USE

# Brute Force API endpoints

