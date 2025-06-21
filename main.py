from request import fetch
from helper_functions import (
    append_string,
    pad_string,
    filter_list,
    randomly_pick_champions,
)
from inputs import choose_selection_method, choose_total_champions, choose_filter_option


def main():
    champion_list = fetch(
        "http://ddragon.leagueoflegends.com/cdn/15.11.1/data/en_US/champion.json"
    )
    counted = list(enumerate(champion_list, 1))

    def format_list_of_champions(iterable):
        string = ""
        for item in iterable:
            string += append_string(pad_string(item[1]["name"]), item[0])
            if item[0] % 5 == 0:
                string += "\n"
        return string

    selection_method = choose_selection_method()
    if selection_method.upper() == "R":
        total_and_filter_picks = (choose_total_champions(), choose_filter_option())
        # print(randomly_pick_champions(champion_list, total_and_filter_picks))
        randomly_pick_champions(champion_list, total_and_filter_picks)
    elif selection_method.upper() == "M":
        print(format_list_of_champions(counted))


if __name__ == "__main__":
    main()
