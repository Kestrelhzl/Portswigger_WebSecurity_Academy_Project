API Testing
===

### Lab: Exploiting an API endpoint using documentation

> To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.

#### Main Points

* Change url path to `/api/user/carlos`.
* Change method to `DELETE`.

<kbd><img width="277" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/179a45bb-368f-4c83-a248-d3fcb4fb2c70"></kbd>

#### POC
```
python3 1_Delete_User.py <base_url>
```
<img width="845" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/6efcd4f0-8f7e-4305-9208-14bdaff117e1" style="border: 2px solid black;">

---

### Lab: Exploiting server-side parameter pollution in a query string

> To solve the lab, log in as the administrator and delete carlos.

#### Main Points

*








---

### Lab: Finding and exploiting an unused API endpoint

> To solve the lab, exploit a hidden API endpoint to buy a Lightweight l33t Leather Jacket. You can log in to your own account using the following credentials: wiener:peter.

#### Main Points

* Change product price (need to add `Content-Type: application/json; charset=utf-8` on header.)
 
  <kbd><img width="963" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/030e0bce-eca6-42c6-94f2-9b18748dffce">
</kbd>

* Add product to cart

  <kbd><img width="871" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/5d669693-539c-4b74-accd-c348e0f3a6f6">
</kbd>

* checkout cart (need to get csrf token from path `/cart` first)
  
  <kbd><img width="1043" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/49fd1ea2-adb0-4651-86ad-5e0d6dfa9805">
</kbd>

#### POC
```
python3 3_Buy_Something.py <base_url>
```
<img width="813" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/621167fe-d875-43a3-888f-24c5b685d5d2">

---

### Lab: Exploiting a mass assignment vulnerability

> To solve the lab, find and exploit a mass assignment vulnerability to buy a Lightweight l33t Leather Jacket. You can log in to your own account using the following credentials: wiener:peter.















