from email import header
import requests
import json
import time

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

URL = "https://emapa.fra1.cdn.digitaloceanspaces.com/statuses.json"


def get_chat_id_and_name(url):
    response = requests.get(url=url, headers=HEADERS)
    response = response.json()['result'][0]['message']['chat']
    try:
        chat_id = int(response['id'])
    except:
        chat_id = ""
    try:
        chat_name = response['title']
    except:
        chat_name = ""
    return chat_id, chat_name


async def get_alarms(url=URL):
    response = requests.get(url=URL, headers=HEADERS)
    alarms = response.json()['states']
    with open(f'../AlarmsSite/alarms.json', 'w') as file:
        json.dump(alarms, file, indent=4, ensure_ascii=False)
    with open(f'alarms.json', 'w') as file:
        json.dump(alarms, file, indent=4, ensure_ascii=False)
    # return alarms


if __name__ == "__main__":
    get_alarms()
