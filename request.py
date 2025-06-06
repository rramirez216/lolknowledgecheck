import requests


def fetch(url):
    response = requests.get(url).json()
    data = response["data"].values()
    new_list = map(
        lambda key: {"id": key["id"], "name": key["name"], "tags": key["tags"]},
        data,
    )
    # return list(response["data"].values())
    print(list(new_list))


fetch("http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json")
