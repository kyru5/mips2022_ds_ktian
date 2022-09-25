#!/usr/bin/python3
import numpy as np
import pandas as pd
import random

import matplotlib.pyplot as plt
import seaborn as sns
from kaggle_environments import make, evaluate, utils

#env = make("rps", debug=True)
# env.reset()

outcomes = evaluate(
   "rps",  # environment to use - no need to change
   agents=["rock_agent.py", "paper_agent.py"],  # agents to evaluate
   num_episodes=1,
   steps=10,
   debug=True,
   configuration={"episodeSteps": 2}  # number of episodes
)

print(outcomes)

#env = make("rps", debug=True)
# env.reset()
#l = env.run(["paper_agent.py", "scissor_agent.py"])
#env.render(mode="ipython", width=700, height=550)
