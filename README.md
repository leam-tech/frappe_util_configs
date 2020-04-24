## Frappe Util Configs

Useful frappe features for your random purposes


### Installation
```
$ bench get-app https://github.com/leam-tech/frappe_util_configs
```
You dont have to install this app in any frappe site. Please follow the sections below to make use of those features

### JWT
JSON WebToken are easy to work with compared to Session Cookies. We present you JWT Support in frappe.
- To start using this, please run the following:
  ```
  $ bench frappe-util-configs init
  ```
  This command will update the `config/supervisor.conf` to use `frappe_util_configs.app:application` as gunicorn entry point and replaces default `frappe/socket.io` with `frappe_util_configs/socket.io`

- To obtain a token, pass `use_jwt: 1` along with email and password
  ```
  POST /api/method/login
  {
    "usr": "administrator",
    "pwd": "my-pwd",
    "use_jwt": 1
  }

  ```
  You will get the token in the response

- To use the token, pass it in `Authorization` header
  ```
  POST /api/method/frappe.auth.get_logged_user
  Authorization: JWT <token>
  ```


### CORS
Cross Origin Resource Sharing might be required when you have custom applications running
To have the CORS headers available in production mode, run
```
$ bench frappe-util-configs nginx
```


#### License

MIT