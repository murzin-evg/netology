import os
from pprint import pprint

def recipes():
    current = os.getcwd()
    folder = 'oop'
    file = 'recipes.txt'

    full_path = os.path.join(current, folder, file)

    cook_book = {}

    with open(full_path, 'rt', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            count = int(file.readline().strip())

            cook_book[dish_name] = []

            for _ in range(count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                
                cook_book[dish_name].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            file.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes()
    result = {}

    for dish_name in dishes:

        for ingredient in cook_book[dish_name]:

            if ingredient['ingredient_name'] not in result:

                result[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))