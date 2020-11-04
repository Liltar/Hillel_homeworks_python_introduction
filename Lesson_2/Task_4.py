# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите `YES`, иначе выведите `NO`.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

some_input = input('Enter number: ')
try:
    val = int(some_input)
    if (int(some_input) % 4) == 0 and int(some_input) % 100 != 100 and int(some_input) % 400:
        print(some_input, 'is a leap year')
    else:
        print(some_input, 'is a common year')
except ValueError:
    try:
        val = float(some_input)
        print('Input is a float number')
    except ValueError:
        print('Input is a string')