from random import *
from os import *
from time import *
a = []

print('\n' * 15, ' ' * 109, 'Приветствую Вас!\n',' ' * 106, 'Что пожелаете делать?')
d = str(input(' ' * 119))
if d == 'Хочу расслабиться':
    system('cls||clear')
    system('color a')
    for i in range(63):
        for h in range(237):
            c = randint(0,1)
            a.append(c)
        print(*a, sep = '')
        sleep(0.01)
        a = []
    for l in range(63):
        print(' ')
        sleep(0.01)
system('color f')
system('cls||clear')
for p in range(3):
    for o in range(3):
        print('\n' * 15, ' ' * 117, 'Загрузка', '.' * (o + 1))
        sleep(0.5)
        system('cls||clear')
print('\n' * 15, ' ' * 107, 'Включаю расслабляющую музыку', sep = '')
sleep(0.5)
startfile('music.mp3')
sleep(3)
system('cls||clear')
sleep(10)
