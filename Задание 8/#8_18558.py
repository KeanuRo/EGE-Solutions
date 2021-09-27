#8 задание ЕГЭ
#Сколько 5-буквенных кодов может составить Иван, если в каждом слове хотя бы одно 'И'?
#https://inf-ege.sdamgia.ru/problem?id=18558
letters = 'ИВАН'
k = 0 #Счётчие
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters: #5-мерный перебор для всех букв
                    word = a + b + c + d + e #Составляем слова
                    if word.count('И'): #Если обнаружено хотя-бы одно 'И', то засчитываем его
                        k += 1
print(k)