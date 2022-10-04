#!/usr/bin/python3

import json
import pandas as pd

df = pd.read_csv('data/recipes.csv')

ingredients = list(df.columns[3:])
ids = list(df['id'].unique())

def make_list(df):
    l = []
#    for i, j in zip(ingredients, list(df)[3:]):
#        if j == 1:
#            print('j==1')
#            l.append(i)
    for i in ingredients:
        if df[i].item() == 1:
            l.append(i)
    return l

new_recipes = [] # Создаём пустой список для хранения итоговой структуры
for current_id in ids: # Организуем цикл с параметром current_id
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0] # Получаем значение соответствующей кухни, применив фильтр по текущему значению параметра цикла к DataFrame;
    current_ingredients = make_list(df[df['id'] == current_id]) # Получаем перечень ингредиентов, входящих в состав текущего блюда
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients} # Создаём текущий словарь
    new_recipes.append(current_recipe) # Добавляем созданный словарь к списку
    
new_recipes = json.dumps(new_recipes) # Функция dumps() модуля json сериализирует объект Python в строку формата JSON. 
with open("data/new_recipes.json", "w") as write_file: # Откроем файл new_recipes.json для записи
    write_file.write(new_recipes) # Записываем содержимое подготовленные данные в файл