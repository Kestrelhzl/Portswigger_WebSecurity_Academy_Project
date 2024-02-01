API Testing Lab Writeup
===

### Lab: Exploiting an API endpoint using documentation

> To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.

1. Login with wiener. And Use the updating email function to update email to `wiener1@normal-user.net`. Use Burp to intercept the packet.

<img width="803" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/65562e17-5787-476f-9569-857dd3ed9223">
<img width="949" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/7e3cf639-4477-4921-9be4-abc3d96d9b12">

2. We can found the URL path is `/api/user/wiener`. And the http method is `PATCH`.

<img width="505" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/cd9a3c6d-b95f-4212-8146-e2ab6744e5a8">

3. Change the url path to `/api/user/carlos` and http method to `DELETE`.
<img width="611" alt="image" src="https://github.com/Kestrelhzl/Portswigger_WebSecurity_Academy_Project/assets/158291600/5179ad25-e978-4806-ba3a-4dc633e0f2e3">

