#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:37:15 2022

@author: keyreeltian
"""

import pandas as pd

"""
def create_medications(names, counts):
    return pd.Series(counts, index=names)


def get_percent(medications, name):
    tot = 0
    for m in medications:
        tot += m
    return (medications[name] / tot) * 100

if __name__ == '__main__':
    names=['chlorhexidine', 'cyntomycin', 'afobazol']
    counts=[15, 18, 7]
    medications = create_medications(names, counts)
    print(get_percent(medications, "chlorhexidine"))
"""


def create_companyDF(incomes, expenses, years):
    # ваш код здесь
    df = pd.DataFrame({'income': incomes, 'expenses': expenses}, index=years)
    return df


def get_profit(df, year):
    # ваш код здесь
    profit = df['income'].loc[year] - df['expenses'].loc[year]
    return profit


if __name__ == '__main__':
    expenses = [156, 130, 270]
    incomes = [478, 512, 196]
    years = [2018, 2019, 2020]

    scienceyou = create_companyDF(incomes, expenses, years)
    print(get_profit(scienceyou, 2020))
