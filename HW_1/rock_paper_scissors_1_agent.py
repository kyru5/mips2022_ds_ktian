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

counter = 0

# Каждый 3й ход - "камень", каждый с остатком 1 после деления на 3 - "бумага",
# в остальных случаях "ножницы"
def rock_paper_scissors(observation, configuration):
    global counter

    if observation.step > 0:
        if counter % 3 == 0:
            your_action = 0
            counter += 1            
        elif counter % 3 == 1:
            your_action = 1
            counter += 1
        else:
            your_action = 2
            counter += 1
        
        return your_action

    else:
        return random.randrange(0, configuration.signs)
