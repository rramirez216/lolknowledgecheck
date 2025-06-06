import requests


def create_new_dict(iterable):
    return list(
        map(
            lambda key: {"id": key["id"], "name": key["name"], "tags": key["tags"]},
            iterable,
        )
    )


def fetch(url):
    response = requests.get(url).json()
    data = response["data"].values()
    return create_new_dict(data)
