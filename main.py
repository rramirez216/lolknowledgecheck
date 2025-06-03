from request import fetch


def main():
    print(
        fetch("http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json")
    )


if __name__ == "__main__":
    main()
