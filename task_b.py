#------------------------------------------------------------------------------------
# Функция, которая считает количество гласных в слове.
def count_vowels(word):
    count = 0
    vowels = "aeiouаеёиоуыэюя"
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count
# Функция, которая считает слова, содержащие более трех гласных букв.
def result_words(word_list):
    result = []
    for word in word_list:
        vowel_count = count_vowels(word)
        if vowel_count > 3:
            result.append(word)
    return result
#------------------------------------------------------------------------------------
# Ввод/вывод
word_list = input("Введите список слов через пробел: ").split()
print("Слова с более чем тремя гласными буквами:", result_words(word_list),'\n')
#------------------------------------------------------------------------------------