from email import header
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_text(id: int) -> str:
    headers = {
        'user-agent': UserAgent().random,
    }

    response = requests.get(
        url=f"https://news.ycombinator.com/item?id={id}", headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    body = soup.find("div", class_="comment")

    return body.text.strip()
