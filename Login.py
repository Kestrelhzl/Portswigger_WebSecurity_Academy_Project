# Testing on Portswigger Academy Lab - API Testing - Lab: Exploiting an API endpoint using documentation
# To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.
# Credit: Kestrel.hzl

import requests
import sys
from bs4 import BeautifulSoup

args = sys.argv[1:]

if len(sys.argv)<4:
    print("python3 login.py <url> <username> <password>")
    sys.exit(1)

target_url = args[0]
username = args[1]
password = args[2]

# Get the CSRF Token
def get_csrf_token(target_url, session):

    print("> Getting CSRF_Token")

    response = session.get(target_url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        csrf_input = soup.find("input", {"name": "csrf"})

        if csrf_input:
            csrf_token = csrf_input["value"]
            return csrf_token
        
        else:
            print("[!] CSRF Token not found.")
            return None, None
    
    else:
        print("[!] Web Request Error.")
        return None

# Perform Login
def login(target_url, username, password, csrf_token, session):

    print("> Logining")
    
    data = "csrf="+csrf_token+"&username="+username+"&password="+password

    response = session.post(target_url, data=data)

    if response.status_code == 200:
        if "Invalid username or password" not in response.text:
            print("login successfully")
            print("Login Cookie: session =",session.cookies.get('session'))
        else:
            print("Error credential.")

    else:
        print("[!] login failed.")
        print(response.status_code)
 

# Create Session
session = requests.session()

csrf_token = get_csrf_token(target_url, session)

if csrf_token:
    print("CSRF_Token: ",csrf_token)
    login(target_url, username, password, csrf_token, session)
    
else:
    sys.exit(1)




