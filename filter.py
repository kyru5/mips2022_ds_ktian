#!/usr/bin/python3

def family(*args):
    family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]
    # ваш код здесь. используйте функцию filter()
    return list(filter(lambda x: x in family_list, args))

#вызов функции
print(family(
    'newborn registration',
    'parking permit',
    'maternity capital',
    'tax benefit',
    'medical policy'
    )
)