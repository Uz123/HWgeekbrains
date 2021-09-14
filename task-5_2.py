n = int(input("Введите верхнюю границу диапазона: "))


def odd_num(extreme):
    odd_num_gen = [num for num in range(1, extreme + 1, 2)]
    return odd_num_gen


print(odd_num(n))
