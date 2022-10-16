#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:29:03 2022

@author: keyreeltian
"""

import pandas as pd
import os

pd.set_option('display.max_columns', None)

# Перейдем в директорию для ДЗ
os.chdir('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/HW_2')

# Откроем наши данные
tdf = pd.read_csv('data/train.csv')
ldf = pd.read_csv('data/lectures.csv')
qdf = pd.read_csv('data/questions.csv')

# Исследуем данные train.csv
# df = tdf.describe()
# df.to_csv('tdf_describe.csv', index=True, sep=';')
# tdf.info() RangeIndex: 101_230_332 entries, 0 to 101_230_331

# Посчитаем студентов в базе?
# print(tdf.user_id.nunique())   # 393_656 students
users = set(tdf.user_id)   # 393_656 students

# Проверим, в каких столбцах есть NaN
# и увидим, что только столбцы prior_question_elapsed_time и 
# prior_question_had_explanation содержат пустые значения
tdf.isna().mean()   

# Сформируем словарь из таких студентов и кол-ва посещенных ими лекций
lecture_users = tdf[tdf.user_answer == -1].user_id.value_counts().to_dict()
# Сколько студентов посещали лекции?
# print(len(lecture_users)) #149_606 студентов

# Ранжируем студентов по кол-ву правильных ответов и создадим словарь
users_correct = tdf[tdf.answered_correctly == 1].user_id.value_counts().to_dict()

# Ранжируем студентов по кол-ву неправильных ответов и создадим словарь
users_incorrect = tdf[tdf.answered_correctly == 0].user_id.value_counts().to_dict()

df = tdf.head(1000)


#df = tdf[tdf.isna().any(axis=1)][tdf.timestamp != 0]
#df.to_csv('tdf_isna.csv', index=True, sep=';')

def tags2list (series):
    tl = series.split(sep=' ')
    return tl
    