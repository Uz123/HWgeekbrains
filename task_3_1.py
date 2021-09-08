num_ar = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(en_number):
    return num_ar.get(en_number)


print(num_translate(input('Введите число от 0 до 10 на английском языке: ')))
