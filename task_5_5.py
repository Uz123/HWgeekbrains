# Решение в "лоб"
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in src if src.count(i) == 1])

# Попытка оптимизации через множество. Мне так и не удалось придумать как сохранить порядок при таком подходе
key = frozenset(src)
result = dict.fromkeys(key, 0)
for key in src:
    result[key] += 1
print([i for i in result if result[i] == 1])
