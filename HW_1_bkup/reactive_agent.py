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

def reactive(observation, configuration):

    if observation.step > 0:
        opponent_action = observation.lastOpponentAction
        your_action = (opponent_action + 1) % 3
        return your_action

    else:
        return 1
