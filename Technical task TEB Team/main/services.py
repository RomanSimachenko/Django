import requests
import json


API_URL = "http://136.244.93.168/admin_api/v1/{}/log"

HEADERS = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Api-Key": "7b88e90dfad2f86bf250b0ac388176ec"
    }


def get_clicks_count(username: str, date_from: str, date_to: str):
    """Gets clicks count through API"""
    clicks = requests.post(
        url=_build_api_url('clicks'),
        headers=HEADERS,
        data=json.dumps(_build_params(username, date_from, date_to, 'datetime'))
    ).json()['total']

    return clicks


def get_conversions_count(username: str, date_from: str, date_to: str):
    """Gets conversions count through API"""
    conversions = requests.post(
        url=_build_api_url('conversions'),
        headers=HEADERS,
        data=json.dumps(_build_params(username, date_from, date_to, 'postback_datetime'))
    ).json()['total']

    return conversions


def _build_api_url(what: str):
    """Builds url for API"""
    return API_URL.format(what)


def _build_params(username: str, date_from: str, date_to: str, what_date: str):
    """Builds params for request"""
    PARAMS = {
        "range": {
            "from": date_from,
            "to": date_to
            },
        "columns": [
            what_date
            ],
        "filters": [
            {
                "name": "sub_id_6",
                "operator": "EQUALS",
                "expression": username
                }
            ],
        "sort": [
            {
                "name": what_date,
                "order": "DESC"
                }
            ]
        }

    return PARAMS
