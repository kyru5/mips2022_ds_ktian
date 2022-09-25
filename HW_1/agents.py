#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils
import random

agents = {
    "rock_agent.py": 0,
    "paper_agent.py": 0,
    "scissors_agent.py": 0,
    "random_agent.py": 0,
    "copy_opponent_agent.py": 0,    
    "rock_paper_agent.py": 0,
    "rock_paper_scissors_1_agent.py": 0,
    "rock_paper_scissors_2_agent.py": 0,
    "smart_1_agent.py": 0,
    "stats_1_agent.py": 0,
    "stats_2_agent.py": 0,
    "stats_3_agent.py": 0
}
