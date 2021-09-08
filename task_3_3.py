name = ["Иван", "Мария", "Петр", "Илья", "Бони", "Клайд"]


def thesaurus(*args):

    sort_names = {}
    for s in sorted(args):
        sort_names.setdefault(s[0], []).append(s)
    return sort_names


print(thesaurus(*name))
