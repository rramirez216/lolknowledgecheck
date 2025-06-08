from request import fetch
from helper_functions import append_string, pad_string


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/15.11.1/data/en_US/champion.json"
    )

    counted = list(enumerate(champion_list, 1))

    def format_list_of_champions(iterable):
        str = ""
        for item in iterable:
            str += append_string(pad_string(item[1]["name"]), item[0])
            if item[0] % 5 == 0:
                str += "\n"
        return str

    print(format_list_of_champions(counted))


if __name__ == "__main__":
    main()
