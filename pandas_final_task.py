#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:34:06 2022

@author: keyreeltian
"""

import pandas as pd

df = pd.read_csv('data/citibike-tripdata.csv')
df1 = df.copy()
#df1['startime'] = pd.to_datetime(df1.starttime, dayfirst=True)
df1 = df1.drop(['start station id', 'end station id'], axis=1)
df1['age'] = 2018 - df1['birth year']
df1.starttime = pd.to_datetime(df1.starttime, dayfirst=True)
df1.stoptime = pd.to_datetime(df1.stoptime, dayfirst=True)

# timedelta64 имеет аксессор total_seconds()
df1['trip duration'] = df1.stoptime - df1.starttime
print(df1['trip duration'].dt.total_seconds().mean())

# или
print(df1['trip duration'].mean().seconds)

df1['weekend'] = df1.starttime.apply(lambda x: 1 if \
                                     (x.weekday() == 5) or \
                                     (x.weekday() == 6) else 0)
print(df1[df1.weekend == 1].shape)

def daytime (hour):
    if 0 <= hour <= 6:
        return 'night'
    elif 6 < hour <= 12:
        return 'morning'
    elif 12 < hour <= 18:
        return 'day'
    else:
        return 'evening'
    
df1['time_of_day'] = df1.starttime.dt.hour.apply(daytime)