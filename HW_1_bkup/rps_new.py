#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils


all_agents = {
    "rock_agent.py": 0,
    "paper_agent.py": 0,
    "copy_opponent_agent.py": 0,    
    "scissors_agent.py": 0,
    "random_agent.py": 0,
    "rock_paper_agent.py": 0,
    "rock_paper_scissors_1_agent.py": 0,
    "rock_paper_scissors_2_agent.py": 0,
    "smart_1_agent.py": 0,
    "stats_1_agent.py": 0,
    "stats_2_agent.py": 0,
    "stats_3_agent.py": 0
}

env = make("rps", debug=True)
env.reset()

agents = list(all_agents.keys())

for a in list(all_agents.keys()):  
    l = []
    agents.pop(0)
    if len(agents) > 0:
        for i in agents:
            l = env.run([a, i])
            if l[-1][0]['reward'] > l[-1][1]['reward']:
                all_agents[a] += 1
                print(a, 'won', i)
            elif l[-1][0]['reward'] < l[-1][1]['reward']:
                all_agents[i] += 1
                print(i, 'won', a)
            
        
print(sorted(all_agents.items(), key=lambda x: x[1], reverse=True))
