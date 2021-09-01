for percent in range(101):
    if percent % 10 == 1 and percent % 100 != 11:
        print(f'{percent} процент')
    elif 1 < percent <= 4 and not 11 < percent % 100 < 15:
        print(f'{percent} процента')
    else:
        print(f'{percent} процентов')
