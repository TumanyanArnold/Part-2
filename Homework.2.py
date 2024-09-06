first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and second == third:
    print('Три числа равны между собой.')
elif (second == first or second == third
      or third == first):
    print('Только 2 числа равны.')
else:
    print('Нет равных чисел.')
