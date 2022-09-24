#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils

# evaluate(
#    "rps",  # environment to use - no need to change
#    ["rock_agent.py", "copy_opponent.py"],  # agents to evaluate
#    configuration = {"episodeSteps": 100}  # number of episodes
#)

env = make("rps", debug=True)
# env.render()

env.reset()

env.run(["rock_paper_scissors_2.py", "stats_3.py"])
env.render(mode="ipython", width=700, height=550)