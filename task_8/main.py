# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

while True:
    try:
        length = int(input('Введите длину шоколадки: '))
        width = int(input('Введите ширину шоколадки: '))
        quantity = int(input('Введите количество кусочков: '))
        if quantity < width * length:
            if (quantity % width == 0 or quantity % length == 0):
                print(f'От шоколадки можно отломить заданное количество кусочков!')
                break
            else:
               print(f'От шоколадки с длиной {length} и шириной {width}'
                     + f' нельзя отломить {quantity} ' 
                     + '(останутся отделенные от шоколадки кусочки которые не нужно было отламывать)')
               break
        elif quantity == width * length:
            print('Шоколадка целиком содержит заданное количество кусочков!')
            break
        else:
            print('Столько кусочков нет!')
            break
    except:
        print('Некорректный ввод!')  