F = 1
G = 1
F1 = 0
for n in range(2, 5):
    F1 = F
    F = 2 * G + 5 * n
    G = F1 + 2 * n
print(F + G)