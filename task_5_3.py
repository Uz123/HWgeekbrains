from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]

classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(tutors) > len(classes):
    pair = (non for non in zip_longest(tutors, classes))
else:
    pair = (non for non in zip(tutors, classes))

print(type(pair))
print(*pair)
