# 1. Программа которая при запуске должна:
#
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
#
# Каждая введённая строка, в файле, должна начинаться с новой строки.

with open('task_1.txt', 'w') as file:
    while True:
        user_input = input('Enter text:')
        file.writelines(user_input + '\n')
        if user_input == '':
            break
