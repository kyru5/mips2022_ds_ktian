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
    
# =====================Работа с датами=========================================

df1.Date = pd.to_datetime(df1.Date, dayfirst=True)
years_sold = df1['Date'].dt.year
df1['MonthSale'] = df1['Date'].dt.month
df1['MonthSale'].value_counts(normalize=True)

df1['AgeBuilding'] = df1.Date.dt.year - df1.YearBuilt

df1.drop('YearBuilt', axis=1, inplace=True)

df1['WeekdaySale'] = df1.Date.dt.dayofweek

#df2 = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')
#df2['Time'] = pd.to_datetime(df2.Time)
#df2['diff'] = df2[df2.State == 'NV'].Time.diff()
#print(df2[df2.State == 'NV']['diff'].dt.days.mean())

# =====================Преобразование столбцов=================================

def get_street_type(address):
# Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type

street_types = df1.Address.apply(get_street_type)
popular_stypes =street_types.value_counts().nlargest(10).index

df1['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
df1.drop('Address', axis=1)

def get_weekend (weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else:
        return 0
    
df1['Weekend'] = df1.WeekdaySale.apply(get_weekend)

top_sellers = df1.SellerG.value_counts()[0:49].index
df1['SellerG'] = df1.SellerG.apply(lambda x: x if x in top_sellers else 'other')
round(df1.Price[df1.SellerG == 'Nelson'].min() / df1.Price[df1.SellerG == 'other'].min(),1)
    
    
    
def get_experience(arg):
    """
    Напишите функцию get_experience(arg), аргументом которой является строка столбца с опытом работы. 
    Функция должна возвращать опыт работы в месяцах. Не забудьте привести результат к целому числу.
    """
    m = None
    years = ['год', 'лет', 'года']
    months = ['месяца', 'месяцев']
    l = arg.split(' ')
    print(l)
    if len(l) == 6:
        if l[3] in years:
            m = int(l[2]) * 12 + int(l[4])
    elif len(l) == 4:
        if l[3] in years:
            m = int(l[2]) * 12
        else:
            m = int(l[2])
    return m

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in df1.columns: # цикл по именам столбцов
    if df1[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        df1[col] = df1[col].astype('category')
        

df1['Type'] = df1['Type'].cat.add_categories('flat')
new_houses_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
new_houses_types = new_houses_types.astype(df1['Type'].dtype)

    
df1.Suburb = df1.Suburb.apply(lambda x: x if x in df1.Suburb.value_counts().nlargest(119).keys() else 'other')
df1.Suburb = df1.Suburb.astype('category')
    
    