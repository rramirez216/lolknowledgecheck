from request import fetch


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
    )
    # for i in range(0, 4):
    # print(champion_list[i])
    print(champion_list[0])


if __name__ == "__main__":
    main()
