# 5. Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'.
# Дать пользователю три попытки ;)

import random
programm_number = random.randint(0, 10)
attempts = 0
user_guess = (input('Enter a number from 1 to 10: '))
while attempts < 3:
    if int(user_guess) == programm_number:
        print('You won!')
    else:
        print('You lose!')