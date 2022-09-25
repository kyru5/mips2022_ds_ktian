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

# Накапливаем статистику ходов оппонента.
# Мой следующий ход на 1цу больше статистически популярного выбора оппонента.
def stats_1(observation, configuration):
    global your_last_action
    global opponent_actions
    d = {}
    if observation.step > 0:
        opponent_actions.append(observation.lastOpponentAction)
        d = {0: opponent_actions.count(0),
                      1: opponent_actions.count(1),
                      2: opponent_actions.count(2)}
        oa_max = max(d.values())

        for key, val in d.items():
            if val == oa_max:
                your_action = (key + 1) % 3

        return your_action

    else:
        your_action = random.randrange(0, 3, 1)
        return your_action
