import requests


def fetch(url):
    data = requests.get(url).json()
    return data["data"]
