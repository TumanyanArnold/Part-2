
def random_sp (number):
    random_dp = list()
    limit_sp = (number + 1) // 2
    for i in range(1, limit_sp):
        p = i + 1
        while i + p <= number:
            if number % (i + p) == 0:
                a_ = (i, p)
                random_dp.append(a_)
            p += 1
    return random_dp

sp_ = True
while sp_:
    first_number = int(input('Введите своё число: '))
    if first_number in range(3, 21):
        sp_ = False
    else:
        print('Введённое число слишком большое, выходит за рамки [3, 21]')
        print('Введите повторно')
print(f'Для числа {first_number} подходят пароли: {random_sp(first_number)}')
