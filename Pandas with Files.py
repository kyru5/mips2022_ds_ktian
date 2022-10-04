#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:12:03 2022

@author: keyreeltian
"""

import pandas as pd

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countries_df.to_csv('countries.csv', index=False, sep=';')

countries_data = pd.read_csv('data/countries.csv', sep=';')

data = pd.read_csv('data/melb_data.csv')

#=======================================================================


melb_data = pd.read_csv('data/melb_data.csv', sep=',')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')

def check_for_coordinates_duplicates (coordinates_series):
    coordinates_set = {}
    for c in list(coordinates_series):
        coordinates_set.append(c)
    if len(coordinates_set) < len(list(coordinates_len)):
        return True
    else:
        return False
    
check_for_coordinates_duplicates(melb_data['Coordinates'])

melb_data[(melb_data.Price < 1000000) & (melb_data.Rooms > 5) | (melb_data.YearBuilt > 2015)]
