from constants import selection_prompt, total_champions_prompt


def choose_selection_method():
    selection_method = input(selection_prompt)
    print("method:", selection_method)
    return selection_method


def choose_total_champions():
    total = input(total_champions_prompt)
    print(total)
