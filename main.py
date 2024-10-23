def single_root_words(root_word, *other_words):
    same_words = []  # Создаём пустой список для подходящих слов

    # Перебираем предполагаемые подходящие слова
    for word in other_words:
        # Условие: слово содержит корень или корень содержится в слове
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)  # Добавляем слово в список

    return same_words  # Возвращаем список подходящих слов

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результат на экран
print(result1)
print(result2)