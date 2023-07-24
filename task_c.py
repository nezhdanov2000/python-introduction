#------------------------------------------------------------------------------------ 
def find_second_longest(list):
    # Проверка наличия минимального количества элементов в списке
    if len(list) < 2:
        return 'Недостаточно элементов в списке'

    # Инициализация первого и второго по длине элементов
    longest = ['']
    second_longest = ['']

    # Поиск наибольшего и второго по длине элементов
    for element in list:
        if len(element) > len(longest[0]):
            second_longest = longest
            longest = [element]
        elif len(element) == len(longest[0]):
            longest.append(element)
        elif len(element) > len(second_longest[0]):
            second_longest = [element]
        elif len(element) == len(second_longest[0]):
            second_longest.append(element)

    # Проверка на наличие второго по длине элемента
    if second_longest == ['']:
        return 'Второго по длине элемента нет'
    else:
        return second_longest
#------------------------------------------------------------------------------------ 
# Ввод/вывод
list = input('Введите список элементов через пробел: ').split()
print('Список вторых по длине элементов:', find_second_longest(list),'\n')
#------------------------------------------------------------------------------------ 