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
counter = 0

def rock_paper_scissors_2(observation, configuration):
    global your_last_action
    global counter

    if observation.step > 0:
        if counter % 2 == 0:
            your_action = 0
            counter += 1            
        elif counter % 3 == 0:
            your_action = 1
            counter += 1
        else:
            your_action = 2
            counter += 1
        
        return your_action

    else:
        return random.randrange(0, configuration.signs)
