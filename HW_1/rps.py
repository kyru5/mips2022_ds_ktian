#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils

# Словарь, где ключи - имена файлов с функциями-агентами,
# и значения - счетчики побед в серии из 1000 игр с каждым оппонентом

all_agents = {
    "rock_agent.py": 0,
    "paper_agent.py": 0,
    "scissors_agent.py": 0,
    "copy_opponent_agent.py": 0,    
    "random_agent.py": 0,
    "rock_paper_agent.py": 0,
    "rock_paper_scissors_1_agent.py": 0,
    "rock_paper_scissors_2_agent.py": 0,
    "smart_1_agent.py": 0,
    "stats_1_agent.py": 0,
    "stats_2_agent.py": 0,
    "stats_3_agent.py": 0
}

winners = []  # Список победителей

# Инициируем игровое окружение Kaggle
env = make("rps", debug=True)
env.reset()

# Создаем список агентов - файлов с функциями-агентами
agents = list(all_agents.keys())

# Главный цикл турнира, где каждый агент играет 1000 игр с каждым агентом-оппонентом
for a in list(all_agents.keys()):  
    agents.pop(0)
    if len(agents) > 0:
        for i in agents:
            # Запускаем 1000 игр между парой агентов и сохраняем список аттрибутов в список
            l = env.run([a, i])

            # В последнем элементе списка хранится пара наборов аттрибутов с накопленными
            # счетчиками. Нас интересует счетчик reward (кол-во побед).
            # Определяем победителя и увеличиваем соответствующий счетчик в all_agents
            if l[-1][0]['reward'] > l[-1][1]['reward']:
                all_agents[a] += 1
                print(a, 'won', i)
            elif l[-1][0]['reward'] < l[-1][1]['reward']:
                all_agents[i] += 1
                print(i, 'won', a)
            
# Выводим список пар (агент, кол-во побед)        
all_agents_sorted = sorted(all_agents.items(), key=lambda x: x[1], reverse=True)
print(all_agents_sorted)

max_wins = all_agents_sorted[0][1]

winners = list(filter(lambda x: x[0] if x[1] == max_wins else None, all_agents_sorted))

# Выводим победителей
for i in winners:
    print("\nАгент {} одержал {} побед и стал победителем турнира\n".format(i[0], i[1]))
