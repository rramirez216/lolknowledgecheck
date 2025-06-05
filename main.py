from request import fetch


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
    )
    for x in champion_list:
        print(champion_list[x]["title"])


if __name__ == "__main__":
    main()
