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
# Каждый четный ход играем "камень", каждый нечетный "бумага"
def rock_paper(observation, configuration):
    global counter

    if observation.step > 0:
        if counter % 2 == 0:
            your_action = 0
            counter += 1            
        else:
            your_action = 1
            counter += 1
        
        return your_action

    else:
        return random.randrange(0, configuration.signs)
