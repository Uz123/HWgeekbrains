from itertools import zip_longest
with open('users_hobby.txt', 'w', encoding='utf-8') as f, \
        open('users.csv', 'r', encoding='utf-8') as f_name, \
        open('hobby.csv', 'r', encoding='utf-8') as f_hob:
    names = [i for i in f_name]
    hobby = [i for i in f_hob]
    if len(names) > len(hobby):
        for user, hob in zip_longest(names, hobby):
            f.write("{}: {}".format(str(user).replace(',', ' ').rstrip('\n'), str(hob)))
    else:
        for user, hob in zip(names, hobby):
            f.write("{}: {}".format(str(user).replace(',', ' ').rstrip('\n'), str(hob)))
