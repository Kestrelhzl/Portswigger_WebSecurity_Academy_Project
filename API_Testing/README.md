API Testing
===

### Lab: Exploiting an API endpoint using documentation

> To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.

* Change url path to `/api/user/carlos`.
* Change method to `DELETE`.

<kbd><img width="277" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/179a45bb-368f-4c83-a248-d3fcb4fb2c70"></kbd>

###### POC
```
python3 1_Delete_User.py <base_url>
```
<img width="845" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/6efcd4f0-8f7e-4305-9208-14bdaff117e1" style="border: 2px solid black;">

---

### Lab: Finding and exploiting an unused API endpoint

> To solve the lab, exploit a hidden API endpoint to buy a Lightweight l33t Leather Jacket. You can log in to your own account using the following credentials: wiener:peter.

* Change product price (need to add `Content-Type: application/json; charset=utf-8` on header.)
<img width="616" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/32d1efa8-0266-413d-b71c-7622cc692ec9">

* Add product to cart
<img width="955" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/120be92e-b183-47da-8bba-f89fc2ba1bee">


* checkout cart


###### POC
```
python3 2_Buy_Something.py <base_url>
```
<img width="813" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/621167fe-d875-43a3-888f-24c5b685d5d2">
