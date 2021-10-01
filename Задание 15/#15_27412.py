#15 задание ЕГЭ
#Для какого наибольшего натурального числа А формула тождественно истинна?
#https://inf-ege.sdamgia.ru/problem?id=27412
def f(x, a): #Составляем формулу
    return (x % a != 0 ) <= ((x % 6 == 0) <= (x % 9 != 0))
for a in range(1, 1001): #Перебор для a
    fl = True #Флаг
    for x in range(1, 1001): #Перебор для x
        if not(f(x, a)): #Начинаем процедуру выхода из цикла, если a не подходит (экономия времени)
            fl = False
        if fl == False: #Выходим из цикла
            break
    if fl:
        print(a)