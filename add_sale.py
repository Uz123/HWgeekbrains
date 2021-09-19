from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as bs:
    sale = f'{round(float(argv[1].replace(",", ".")), 2)}'
    print(f'{str(sale)}', file=bs)
