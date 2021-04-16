import sys
import re

with open(sys.argv[1], 'r', encoding='UTF-8') as f:

    # читаем из файла по одному символу, приводим к нижнему регистру
    # если это буква или "-", собираем слово word
    # если это другой символ, проверяем word на правильность (буквы, макс один дефис подряд)
    # правильные word складываем в словарь, значения - количество слов в тексте

    str_a = f.read(1).lower()
    word = ''
    word_counter = {}
    while str_a:
        if re.fullmatch(r'\w|-', str_a):
            word += str_a
        else:
            if re.fullmatch(r'(?:\w+-)*\w+', word):
                word_counter.setdefault(word, 0)
                word_counter[word] += 1
            word = ''
        str_a = f.read(1).lower()

    # выводим i самых частых слова из словаря

    for i in range(3):
        keymax = max(word_counter, key=word_counter.get)
        print(keymax, word_counter[keymax])
        word_counter.pop(keymax)
