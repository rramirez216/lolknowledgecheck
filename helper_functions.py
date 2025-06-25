from random import randrange


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
    print("we got this far")

    def tag_filter(champ):
        is_true = tag in champ["tags"]
        return is_true

    return list(filter(tag_filter, iterable))


def randomly_pick_champions(champ_list, options_tuple):
    print(len(champ_list), options_tuple)
    filtered_list = filter_list(champ_list, options_tuple[1])
    # print("filtered:", filtered_list)
    new_champ_list = []
    for i in range(options_tuple[0]):
        new_champ_list.append(filtered_list[randrange(len(filtered_list))])
    print(new_champ_list)
    return new_champ_list


# TODO: figure out why the Error "empty range for randrange()" is being printed
