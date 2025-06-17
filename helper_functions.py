def append_string(name, count):
    new_str = f"{name} | "
    count = f"{str(count)}."
    if len(count) < 4:
        count = count.ljust(4)

    def preppend_string(appended):
        return f"{count} {appended}"

    return preppend_string(new_str)


def pad_string(string):
    string = string
    length = len(string)
    if length < 14:
        string = str.ljust(14)
    return string


def filter_list(iterable, tag):
    if tag == "All":
        return iterable

    # filter by the tag and return the filtered list


def randomly_pick_champions():
    pass
