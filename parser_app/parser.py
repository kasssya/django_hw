import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://manybooks.net/"
URL = "https://manybooks.net/search-book?sticky=1"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}
@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="content")
    book = []

    for item in items:
        book.append(
            {
                "title": item.find("div", class_="field").find("a"),
                "image": HOST + item.find("div", class_="field").find("img").get("src"),
            }
        )
    return book


@csrf_exempt
def parser_func():
    html = get_html(URL)
    if html.status_code == 200:
        book = []
        for page in range(0, 1):
            html = get_html(URL, params={"page": page})
            book.extend(get_data(html.text))
            return book
    else:
        raise ValueError("Error maybe permission denied")