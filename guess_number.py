from random import *


n = randint(1, 100)
print('Угадайте число от 1 до 100')

def is_valid(s):
    if 1 <= s <= 100:
        return True
    else:
        return False

flag = False

while flag == False:

    d = int(input())

    if is_valid(d):
        if d < n:
            print('Ваше число меньше того, что загадано')
            flag = False
        elif d > n:
            print('Ваше число больше того, что загадано')
            flag = False
        elif d == n:
            print('Отличная интуиция! Вы угадали число ')
            flag = True
    else:
        flag = False


