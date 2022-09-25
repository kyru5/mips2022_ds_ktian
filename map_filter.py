#!/usr/bin/python3

names = ['Ivan', 'Nikita', 'Simon', 'Margarita', 'Vasilisa', 'Kim']

#print(list(filter(lambda x: len(x) >= 5, names)))
print(list(map(lambda x: (x, x.upper().count('A')), list(filter(lambda x: len(x) >= 5, names)))))