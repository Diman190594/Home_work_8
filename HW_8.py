# from pathlib import Path


# file_path = Path('info', 'data.txt')
# # file_path = r'info\new.txt'
# print(file_path)

# with open(file_path, 'r', encoding='utf8') as text_file:
#     for line in text_file:
#         print(line.strip())


# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def readAll(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def write_1(nm):
    str_new1 = input('Фамилия')
    str_new2 = input('Имя')
    str_new3 = input('Отчество')
    str_new4 = input('Телефон')
    str_new = '\n' + str_new1 + ', ' + str_new2 + ', ' + str_new3 + ', ' + str_new4
    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)

def find_item(nm):
    item = input('Характеристика: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())         

def find_item_Charackeristic(nm):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер поиска (0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)  

def sort_data(nm):
        list_1 = []
        item_type = int(input('Введите номер поиска (0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Телефон): '))
        with open(nm, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                line = line.split(', ')
                list_1.append(line)
            list_1.sort(key= lambda person: person[item_type])
        with open(nm, 'w', encoding='utf8') as txt_file:
            for line in list_1:
                line = ', '.join(line)
                txt_file.write(line)





# write_1('data.txt')
readAll('data.txt')
# find_item('data.txt')
# find_item_Charackeristic('data.txt')
sort_data('data.txt')