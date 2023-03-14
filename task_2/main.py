# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

while True:  
    try:
        number = int(input('Введите трехзначное число: '))
        if 99 < number and number < 1000:
            number_digit_3 = number // 100
            number_digit_2 = (number - number_digit_3 * 100) // 10
            number_digit_1 = number - number_digit_3 * 100 - number_digit_2 * 10
            print(f'Сумма цифр: {number_digit_3 + number_digit_2 + number_digit_1}')
            break
        else: print('Число не трехзначное!')
    except:
        print('Введенное число содержит символы!')
        