#12 задание ЕГЭ
#Что получиться после преобразований?
#https://inf-ege.sdamgia.ru/problem?id=19063
s = '8' * 70 #Число которое нужно преобразовать
while '2222' in s or '8888' in s: #Команда по условию
    if '2222' in s: 
        s = s.replace('2222', '88', 1) # Метод s.replace для замены подстрок согласно условию
    s = s.replace('8888', '22', 1)
print(s) 