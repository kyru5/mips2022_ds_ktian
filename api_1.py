#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:38:19 2022

@author: keyreeltian
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
#response = requests.get(url)

#currencies = response.json()
# pprint(currencies)

# print(currencies['Valute']['CZK']['Name'])

url = 'https://nplus1.ru/news/2021/10/11/econobel2021'
response = requests.get(url)


page = BeautifulSoup(response.text, 'html.parser')
# print(page.title)
# print(page.title.text)
# print(page.find('h1').text)
# print(page.find('time').text)

def wiki(url, tag, cl=''):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    return page.find(tag, class_=cl).text

#print(wiki('https://ru.wikipedia.org/wiki/Pink_Floyd', 'div', 'mw-body'))

#url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'

# response = requests.get(url)
# page = BeautifulSoup(response.text, 'html.parser')
# links = page.find_all('a')

# print([link.text for link in links[0:10]])



token = '2c2ef41a2c2ef41a2c2ef41afb2f3e12c822c2e2c2ef41a4f165eecc64263884ea30554'
url = 'https://api.vk.com/method/users.get'
#params = {'user_id': 1, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'}
#response = requests.get(url, params=params)
# print(response.text)
# print(response.json())

# Метод users.get() позволяет запрашивать информацию о множестве (до 1 000) 
# пользователей одновременно. Для этого нужно использовать параметр user_ids и 
# передавать id через запятую в строковом формате. Например, чтобы получить 
# информацию о пользователях с id=1, id=2, id=3, необходимо передать значение 
# параметра user_ids='1,2,3'.

ids = ",".join(map(str, range(1, 501)))
params = {'user_ids': ids, 'v': 5.95, 'fields': 'sex', 'access_token': token, 'lang': 'ru'}
response = requests.get(url, params=params)

user = response.json()['response'][0]

# Работа с группами VK
url = 'https://api.vk.com/method/groups.getMembers'
#params = {'group_id': 'vk', 'v': 5.95, 'access_token': token}
#response = requests.get(url, params = params)
#data = response.json()
#print(data)

url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
count = 5 
offset = 0 
user_ids = [] 
max_count = 20 
#while offset < max_count: 
    # Будем выгружать по count=5 пользователей, 
    # начиная с того места, где закончили на предыдущей итерации (offset) 
#    print('Выгружаю {} пользователей с offset = {}'.format(count, offset))   
#    params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
#    response = requests.get(url, params = params) 
#    data = response.json() 
#    user_ids += data['response']['items'] 
    # Увеличиваем смещение на количество строк, которое мы уже выгрузили 
#    offset += count 
#print(user_ids) 

# Боремся с ограничением по частоте запросов

import requests # Импортируем модуль requests
import time # Импортируем модуль time
url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес страницы, к которой делаем запрос
count = 1000 
offset = 0  
user_ids = []  
#while offset < 5000: 
#    params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
#    response = requests.get(url, params = params) 
#    data = response.json() 
#    user_ids += data['response']['items'] 
#    offset += count 
#    print('Ожидаю 0.5 секунды...') 
#    time.sleep(0.5) 
#print('Цикл завершен, offset =',offset) 


url = 'https://api.vk.com/method/wall.get' # Указываем адрес страницы, к которой делаем запрос
params = {'domain': 'vk', 'filter': 'owner', 'count': 3, 'offset': 0, 'access_token': token, 'v': 5.95} 
response = requests.get(url, params = params) 
pprint(response.json()['response']['items'][0]['text'][:30]) 


