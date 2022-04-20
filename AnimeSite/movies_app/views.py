from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
import requests


HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
}

FILTERS = "?token=4e72f5db593a7bc7472833379e1a799e&limit=10&types=anime&with_material_data=true"


def IndexPage(request):
    page = request.GET.get('page', None)
    q = request.GET.get('q', None)

    if page:
        json_response = requests.get(
            url="https://kodikapi.com/list" + FILTERS + f"&page={page}", headers=HEADERS).json()
    elif q:
        json_response = requests.get(
            url="https://kodikapi.com/search" + FILTERS + f"&title={q}", headers=HEADERS).json()
    else:
        json_response = requests.get(
            url="https://kodikapi.com/list" + FILTERS, headers=HEADERS).json()

    try:
        next_page = json_response['next_page'].split(
            "page=")[-1] if "page=" in json_response['next_page'] else None
    except:
        next_page = None

    try:
        prev_page = json_response['prev_page'].split(
            "page=")[-1] if "page=" in json_response['prev_page'] else None
    except:
        prev_page = None

    context = {
        "movies": json_response['results'],
        "next_page": next_page,
        "prev_page": prev_page,
        "current_year": datetime.now().year
    }

    return render(request, "movies_app/index.html", context=context)


def DetailMovieView(request, pk):
    json_response = requests.get(
        url=f"https://kodikapi.com/search" + FILTERS + f"&id={pk.strip()}", headers=HEADERS).json()
    movie = json_response['results'][0] if json_response['results'] else {}
    context = {
        "movie": movie,
        "current_year": datetime.now().year,
        "poster_id": movie['material_data']['poster_url'].split("/")[-1].split(".")[0],
    }
    return render(request, "movies_app/movie_detail.html", context=context)


def PlayerView(request, pk):
    json_response = requests.get(
        url=f"https://kodikapi.com/search" + FILTERS + f"&id={pk.strip()}", headers=HEADERS).json()

    context = {
        "movie": json_response['results'][0] if json_response['results'] else {},
    }
    return render(request, "movies_app/player.html", context=context)
