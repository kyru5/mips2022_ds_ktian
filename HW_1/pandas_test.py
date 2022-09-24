#!/usr/bin/python3

import pandas as pd
from IPython.display import display
from chardet.universaldetector import UniversalDetector


detector = UniversalDetector()

with open('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/students_performance.zip', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
# print(detector.close())

data = pd.read_csv('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/students_performance.zip', encoding='koi8-r')
#compression_opts = dict(method='zip', archive_name='out.csv')
#data.to_csv('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/out.zip', index=False, compression=compression_opts)

#data = pd.read_table('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/students_performance.zip', sep=',')

#data = pd.read_excel('https://github.com/asaydn/test/raw/master/january.xlsx')
grades = pd.read_excel('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/grades.xlsx', sheet_name='Maths')
grades.to_excel('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/grades_new.xlsx', sheet_name='Example', index=False)

ratings = pd.read_excel('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/ratings+movies.xlsx', sheet_name='ratings')
movies = pd.read_excel('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/ratings+movies.xlsx', sheet_name='movies')
result = pd.merge(ratings, movies, on='movieId')
result.to_excel('/Users/keyreeltian/Documents/GitHub/mips2022_ds_ktian/data/new_ratings+movies.xlsx', sheet_name='ratings_movies', index=False)


print(grades.head())
# print(data.head().columns)
