#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 00:42:06 2022

@author: keyreeltian
"""

import pandas as pd
import os

os.chdir('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data')
df = pd.read_csv('melb_data_ps.csv')

df1 = df.copy()
df1 = df1.drop(['index', 'Coordinates'], axis=1)
# Alternative option
# melb_df.drop(['index','Coordinates'],axis=1,inplace=True)

total_rooms = df1['Rooms'] + df1['Bedroom'] + df1['Bathroom']

df1['MeanRoomsSquare'] = df1.BuildingArea / total_rooms
df1['AreaRatio'] = (df1['BuildingArea'] - df1['Landsize']) / \
    (df1['BuildingArea'] + df1['Landsize'])