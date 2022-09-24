#!/usr/bin/python3

import json
from pprint import pprint
from numpy import unique
import pandas as pd

l = []
s = set()
d = {}

with open('data/recipes.json') as f:
    recipes=json.load(f)

for i in recipes:
    l.append(i['cuisine'])
    s.add(i['cuisine'])

a = [[l.count(i), i] for i in s]



print(max(a))
# pprint(recipes[0]['id'] == 13121)
