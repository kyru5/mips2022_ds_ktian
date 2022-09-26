#!/usr/bin/python3

reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]

new_reg = map(lambda x: (x[0] + ' ' + x[1][0] + '.', x[2], x[3], x[]), filter(lambda x: x[-1] >= 2000, reg))

print(list(new_reg))