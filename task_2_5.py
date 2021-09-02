prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
prices.sort()                       # Сортировка по возрастанию под буквой "b"
for idx in prices:
    fractional = idx % 1 * 100
    print(f'{int(idx)} руб {int(round(fractional, 2)):02d} коп', end=", ")
print()

prices_2 = prices[::-1]             # Сортировка по убыванию в новом списке "с"
for idx in prices_2:
    fractional = idx % 1 * 100
    print(f'{int(idx)} руб {int(round(fractional, 2)):02d} коп', end=", ")
print()

max_prices = sorted(prices)[:-6:-1]  # 5 максимальных значений из списка "d"
for idx in max_prices:
    fractional = idx % 1 * 100
    print(f'{int(idx)} руб {int(round(fractional, 2)):02d} коп', end=", ")
