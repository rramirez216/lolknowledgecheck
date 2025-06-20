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
        string = string.ljust(14)
    return string


def filter_list(iterable, tag):
    if tag == "All":
        return iterable
    return list(filter(lambda champs: tag in champs["tags"], iterable))


def randomly_pick_champions(champs, options):
    pass
    #
