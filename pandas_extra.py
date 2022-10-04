#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:24:16 2022

@author: keyreeltian
"""

import pandas as pd
import os

os.chdir('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data')

wb_data = pd.read_csv('wb_data.csv', index_col = 0)

wb_data.head(9)

wb_data.loc[1:6, ['cname', 'ccodealp']]
wb_data.iloc[1:3, 1]

wb_data.loc[(wb_data.ht_region== 2) & \
                           (wb_data.p_polity2 < 5)]
    
wb_data_rich_dem = wb_data[(wb_data.p_polity2 >= 4) & (wb_data.wdi_gdpcapcur > 30000)]

# Агрегирование данных по группам

wb_data.groupby('ht_region').mean()['p_polity2'].sort_values()

pd.set_option('display.float_format', '{:.2f}'.format)

# Присвоение новых значений
wb_data1 = wb_data
wb_data1['new_column'] = 'some_text'

# Переименование колонок
wb_data.rename(columns={'ccodealp': 'country_code', 'cname': 'country_name'})

# Сортировка
wb_data.sort_values(by='wdi_gdpcapcur', ascending=False, na_position='last')

