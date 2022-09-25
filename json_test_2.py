#!/usr/bin/python3

import json
from pprint import pprint
from numpy import unique
import pandas as pd


# with open('data/recipes.json') as f:
#    recipes=json.load(f)
#df = pd.DataFrame(recipes)

all_ingredients = set()

df = pd.read_json('data/recipes.json')
for i in df['ingredients']:
    for j in i:
        all_ingredients.add(j)


def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
    if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
        return 1 # возвращаем значение 1
    else: # Если ингредиента нет в текущем блюде,
        return 0 # возвращаем значение 0

for ingredient_name in all_ingredients:  # Последовательно перебираем ингредиенты в реестре all_ingredients
    df[ingredient_name] = df['ingredients'].apply(contains)
        

df['ingredients'] = df['ingredients'].apply(len)  # Заменяем список ингредиентов в рецепте на их количество
df.to_csv('data/recipes.csv', index=False)
# print(len(s))


