#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils
import random

def rock(observation, configuration):
    return 0


def paper(observation, configuration):
    return 1


def scissors(observation, configuration):
    return

def copy_opponent(observation, configuration):
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return random.randrange(0, configuration.signs)

def random(observation, configuration):
    return random.randrange(0, 3, 1)

your_last_action = None
counter = 0

def rock_paper(observation, configuration):
    global your_last_action
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

def rock_paper_scissors(observation, configuration):
    global your_last_action
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

def smart_1(observation, configuration):
    global your_last_action

    if observation.step > 0:        
        your_action = (your_last_action - 1) % 3 if your_last_action is not None \
            else random.randrange(0, configuration.signs)
        your_last_action = your_action
        return your_action

    else:
        return random.randrange(0, configuration.signs)
    
opponent_actions = []

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
    
def pattern_2(oa, loa):
    c012 = 0
    c021 = 0
    cone = 0

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

        return pattern_2(opponent_actions, observation.lastOpponentAction)

    else:
        your_action = random.randrange(0, 3, 1)
        return your_action


agents = {
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
