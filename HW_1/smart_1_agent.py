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

# Мой следующий ход на 1 меньше предыдущего (например, если была "бумага", то будет "камень")
def smart_1(observation, configuration):
    global your_last_action

    if observation.step > 0:        
        your_action = (your_last_action - 1) % 3 if your_last_action is not None \
            else random.randrange(0, configuration.signs)
        your_last_action = your_action
        return your_action

    else:
        return random.randrange(0, configuration.signs)
