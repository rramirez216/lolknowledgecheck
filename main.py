from request import fetch


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
    )

    counted = list(enumerate(champion_list, 1))

    def format_list_of_champions(iterable):
        str = ""
        for item in iterable:
            str += f"{item[0]}. {item[1]['name']} | "
            if item[0] % 5 == 0:
                str += "\n"

        return str

    print(format_list_of_champions(counted))
    highest_count = 0
    longest_name = ""
    for champ in champion_list:
        if len(champ["name"]) > highest_count:
            highest_count = len(champ["name"])
            longest_name = champ["name"]
        continue
    print(f"longest: {longest_name}\nlength: {highest_count}")


if __name__ == "__main__":
    main()
