def append_string(name, count):
    new_str = f"{name} | "
    count = f"{str(count)}."
    if len(count) < 4:
        count = count.ljust(4)

    def preppend_string(appended):
        return f"{count} {appended}"

    return preppend_string(new_str)


def pad_string(str):
    str = str
    length = len(str)
    if length < 14:
        str = str.ljust(14)
    return str
