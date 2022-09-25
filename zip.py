#!/usr/bin/python3

def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i

def print_groups(users):
    #ваш код здесь
    for i, j in zip(users, group_gen()):
        print(i, 'in group', j)
        
users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']
print_groups(users)