from constants import (
    selection_prompt,
    total_champions_prompt,
    select_filter_one,
    select_filter_two,
    roles_list,
)


def choose_selection_method():
    selection_method = input(selection_prompt)
    print("method:", selection_method)
    print("\n\n")
    return selection_method


def choose_total_champions():
    total = input(total_champions_prompt)
    print(total)
    print("\n\n")
    return total


def choose_filter_option():
    pairs = enumerate(roles_list, 1)
    print(select_filter_one)
    print("".join([f"{pair[0]}. {pair[1]}  " for pair in pairs]))
    selected_option = input(select_filter_two)
    print("\n filter by:", selected_option)
    print("\n\n")
    return roles_list[int(selected_option) - 1]
