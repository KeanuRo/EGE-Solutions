# Текстовый файл состоит не более чем из 106 символов A, B и C. 
# Определите максимальную длину цепочки вида ABABAB... (составленной из фрагментов AB, последний фрагмент может быть неполным).
#Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('/home/keanu/Documents/Works/Visual Studio/Python Projects/zadanie24_1.txt', 'r') as file:
    s = file.readline()
    k = 0
    kmax = 0
    for i in range(1, len(s)):
        if s[i] == 'A' and k % 2 == 0 or s[i] == 'B' and k % 2 == 1:
            k += 1
            if k > kmax:
                kmax = k
        elif s[i] == 'A':
            k = 1
        else:
            k = 0
print(kmax)