import requests 
from bs4 import BeautifulSoup
import sys

def check_url(raw_url):

    return raw_url.rstrip('/')


def get_csrf_token(url, session):

    response = session.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("input", {"name": "csrf"})

        if result:
            print("CSRF token : " + result["value"])
            return result["value"]
        else:
            print("[!] CSRF token not found!")
            sys.exit(1)            
    
    else:
        print("web request error.")


session = requests.Session()

args = sys.argv[1:]
base_url = check_url(args[0])
get_csrf_token(base_url, session)







