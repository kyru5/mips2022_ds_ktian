#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:29:03 2022

@author: keyreeltian
"""

import pandas as pd
import os

# Перейдем в директорию для ДЗ
os.chdir('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/HW_2')

# Откроем наши данные
# tdf = pd.read_csv('data/train.csv', nrows=10000)
tdf = pd.read_csv('data/train.csv')

ldf = pd.read_csv('data/lectures.csv')
qdf = pd.read_csv('data/questions.csv')

# Исследуем данные train.csv
df = tdf.describe()
# df.to_csv('tdf_describe.csv', index=True, sep=';')
# tdf.info() RangeIndex: 101_230_332 entries, 0 to 101_230_331

# Посчитаем студентов в базе?
print(tdf.user_id.nunique())   # 393_656 students

# Проверим, в каких столбцах есть Null
print(tdf.info(show_counts=True))   # Заметим, что Null есть только в последних 2х стобцах

df = tdf[tdf.isna().any(axis=1)][tdf.timestamp != 0]
df.to_csv('tdf_isna.csv', index=True, sep=';')

def tags2list (series):
    tl = series.split(sep=' ')
    return tl
    