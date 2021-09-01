list_cubes = []
all_sum = 0
add_all_sum = 0
for idx in range(1, 1000, 2):
    list_cubes.append(idx ** 3)
for ind, val in enumerate(list_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_cubes[ind]
print(all_sum)

for idx in range(len(list_cubes)):
    list_cubes[idx] += 17
for ind, val in enumerate(list_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        add_all_sum += list_cubes[ind]
print(add_all_sum)
