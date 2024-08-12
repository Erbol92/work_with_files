from pprint import pprint
import os

# формирование кулинарного словаря из файла (принимаем имя тхт документа)


def form_cook_book(filename: str):

    cook_book = {}
    structure = ['ingredient_name', 'quantity', 'measure']
    index_l, index_v = 0, 0
    try:
        with open(f"{filename}.txt", encoding='UTF8') as f:
            data = f.read().split('\n')  # формируем список из строк документа

        for idx, line in enumerate(data):  # построчно перебираем данные
            if line:
                if line.isdigit():  # если строка может быть преобр. в число (кол-во ингридиентов)
                    # запоминаем текущее положение курсора и кол-во ингридиентов
                    index_l, index_v = idx, int(line)
                if not cook_book.get(line) and index_l == 0:  # добавляем блюдо
                    cook_book[line] = []
                    cook_name = line
                if index_l < idx <= index_l + index_v:  # ищем ингридиенты и добавляем в блюдо
                    cook_book[cook_name].append(
                        dict(zip(structure, line.split(' | '))))
            else:  # встречаем пустую строку, обнуляем индексы
                index_l, index_v = 0, 0

        return cook_book

    except Exception as e:
        print(e)

# функция создания словаря с названием ингредиентов и его количества для блюда


def get_shop_list_by_dishes(dishes: list, person_count: int):
    products = {}
    for dish in dishes:
        if book.get(dish):  # проверяем есть ли блюда с кулинарной книге
            # проходим по ингридиентам и формируем новый словарь
            for product in book.get(dish):
                if not products.get(product['ingredient_name']):
                    products[product['ingredient_name']] = {
                        'measure': product['measure'],
                        'quantity': int(product['quantity']) * person_count
                    }
                else:
                    products[product['ingredient_name']
                             ]['quantity'] += int(product['quantity']) * person_count
    return products

# генератор нового файла по условиям задачи


def file_generator(input_path: str):
    try:
        sort_files = {}
        # скинируем директорию с файлами
        for file in os.scandir(input_path):
            if file.is_file():  # проверяем является ли файлом
                # открываем файл и читаем кол-во строк
                with open(f"{input_path}/{file.name}", encoding='UTF8') as f:
                    data = f.readlines()
                    # записываем в словарь имя файлаи кол-во строк
                    sort_files[file.name] = len(data)
                    f.close()
        # сортируем по значениям
        sort_files = sorted(sort_files.items(), key=lambda i: i[1])

        print(sort_files)

        # открываем(создаем) файл для записи+чтения
        with open(f"output/result.txt", 'w+', encoding='UTF8') as fw:
            for file in sort_files:
                # открываем каждый файл для получения текста
                with open(f"{input_path}/{file[0]}", encoding='UTF8') as fr:
                    fw.write(file[0]+'\n')
                    fw.write(str(file[1])+'\n')
                    fw.write(fr.read()+'\n')
            fw.seek(0)
            print(fw.read())
            fw.close()
    except Exception as e:
        print(e)


book = form_cook_book('recipes')

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

file_generator('input')
