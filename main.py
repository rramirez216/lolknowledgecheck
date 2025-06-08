from request import fetch
from helper_functions import append_string, pad_string


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json"
    )

    counted = list(enumerate(champion_list, 1))

    def format_list_of_champions(iterable):
        str = ""
        for item in iterable:
            str += append_string(pad_string(item[1]["name"]), item[0])
            if item[0] % 5 == 0:
                str += "\n"
            # print(append_string(pad_string(item[1]["name"]), item[0]))
            # print(pad_string(item[1]["name"]))

        return str

    print(format_list_of_champions(counted))
    # TODO: find out out to make each entry to the str in format function the same length
    # maybe while loop that checks if the string is == to the longest names length
    # if not the same add spaces to the start and maybe end


# "111._" "_|_"

if __name__ == "__main__":
    main()
