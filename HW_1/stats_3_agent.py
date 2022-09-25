#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate

#0 - rock
#1 - paper
#2 - scissors

your_last_action = None
opponent_actions = []

# Отслеживаем паттерны у оппонента и, если находим, планируем свой следующий ход
# В отличие от предыдущей версии агента, в этой версии добавлен еще один паттерн
def pattern(oa, loa):
    c012 = 0  # Инициализируем счетчик паттерна "камень-бумага-ножницы"
    c021 = 0  # Инициализируем счетчик паттерна "камень-ножницы-бумага"
    cone = 0  # Инициализируем счетчик паттерна - один повторяющийся знак

    if len(oa) > 3:
        for i in range(len(oa)):
            if (len(oa) - i) > 3 and oa[i] == 0 and oa[i + 1] == 1 and oa[i + 2] == 2:
                c012 += 1
            if (len(oa) - i) > 3 and oa[i] == 0 and oa[i + 1] == 2 and oa[i + 2] == 1:
                c021 += 1
            if (len(oa) - i) > 3 and oa[i] == 0 and oa[i + 1] == 0 and oa[i + 2] == 0:
                cone += 1
            if (len(oa) - i) > 3 and oa[i] == 1 and oa[i + 1] == 1 and oa[i + 2] == 1:
                cone += 1
            if (len(oa) - i) > 3 and oa[i] == 2 and oa[i + 1] == 2 and oa[i + 2] == 2:
                cone += 1
                
        d = {'012': c012 / (len(oa) // 3), '021': c021 / (len(oa) // 3), 'one': cone / (len(oa) // 3)}

        if d['012'] == max([d['012'], d['021'], d['one']]):
            ptrn = '012'
        elif d['021'] == max([d['012'], d['021'], d['one']]):
            ptrn = '021'
        elif d['one'] == max([d['012'], d['021'], d['one']]):
            ptrn = 'one'
        
        if d[ptrn] > 0.33:
            if ptrn == '012':
                return (loa + 2) % 3
            elif ptrn == '021':
                return loa % 3
            elif ptrn == 'one':
                return (loa + 1) % 3
        else:
            return random.randrange(0, 3, 1)
    else:
        return loa


def stats_3(observation, configuration):
    global your_last_action
    global opponent_actions

    if observation.step > 0:
        opponent_actions.append(observation.lastOpponentAction)

        return pattern(opponent_actions, observation.lastOpponentAction)

    else:
        your_action = random.randrange(0, 3, 1)
        return your_action