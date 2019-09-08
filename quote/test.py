import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get("https://hotel.meituan.com/shanghai/", headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.text)

