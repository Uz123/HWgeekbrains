import random
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat_words):
    """
    Функция get_jokes(), возвращающает n шуток, сформированных из трех случайных слов,
    взятых из трёх списков (по одному из каждого):

    :param n: колличество сформированных шуток
    :param repeat_words: вкл/выкл режима повтора слов, принмает значения True/False
    :return: возращает список joke_list c шутками

    Note:
        Функцция возращает шутку в следующем порядке: существительное, наречие, прилагательное.
        Иной порядок не предусмотрен
    """
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    joke_list = []
    if not repeat_words:
        for name, login, role in zip(nouns, adverbs, adjectives):
            joke = f'{name} {login} {role}'
            joke_list.append(joke)
    else:
        while n > 0:
            joke_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            n -= 1
    return joke_list


print(get_jokes(5, True))
