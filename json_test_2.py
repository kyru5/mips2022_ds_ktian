#!/usr/bin/python3

import json
from pprint import pprint
from numpy import unique
import pandas as pd


# with open('data/recipes.json') as f:
#    recipes=json.load(f)
#df = pd.DataFrame(recipes)

s = set()

df = pd.read_json('data/recipes.json')
for i in df['ingredients']:
    for j in i:
        s.add(j)


def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
    if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
        return 1 # возвращаем значение 1
    else: # Если ингредиента нет в текущем блюде,
        return 0 # возвращаем значение 0

print(len(s))

