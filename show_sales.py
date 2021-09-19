from sys import argv
from itertools import islice

with open('bakery.csv', 'r', encoding='utf-8') as bs:
    if len(argv) == 2:
        i = argv[1]
        content = islice(bs, int(i)-1, None)
        for line in content:
            print(line.strip())
    if len(argv) == 3:
        i, r = argv[1:]
        content = islice(bs, int(i)-1, int(r))
        for line_2 in content:
            print(line_2.strip())
    else:
        content = bs.readlines()
        for line in content:
            print(line.strip())
