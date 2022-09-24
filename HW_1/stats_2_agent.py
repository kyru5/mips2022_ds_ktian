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

def pattern(oa, loa):
    c012 = 0
    c021 = 0

    if len(oa) > 3:
        for i in range(len(oa)):
            if (len(oa) - i) > 3 and oa[i] == 0 and oa[i + 1] == 1 and oa[i + 2] == 2:
                c012 += 1
            if (len(oa) - i) > 3 and oa[i] == 0 and oa[i + 1] == 2 and oa[i + 2] == 1:
                c021 += 1
        d = {'012': c012 / (len(oa) // 3), '021': c021 / (len(oa) // 3)}
        ptrn = '012' if d['012'] > d['021'] else '021'

        if d[ptrn] > 0.33:
            if ptrn == '012':
                return (loa + 2) % 3
            else:
                return loa % 3
        else:
            return random.randrange(0, 3, 1)
    else:
        return loa


def stats_2(observation, configuration):
    global your_last_action
    global opponent_actions

    if observation.step > 0:
        opponent_actions.append(observation.lastOpponentAction)

        return pattern(opponent_actions, observation.lastOpponentAction)

    else:
        your_action = random.randrange(0, 3, 1)
        return your_action