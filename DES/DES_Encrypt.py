InitialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]
"""Начальная перестановка"""

FinalPermutation = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]
"""Конечная перестановка"""

KeyPreparation = [57, 49, 41, 33, 25, 17, 9, 1,
                  58, 50, 42, 34, 26, 18, 10, 2,
                  59, 51, 43, 35, 27, 19, 11, 3,
                  60, 52, 44, 36, 63, 55, 47, 39,
                  31, 23, 15, 7, 62, 54, 46, 38,
                  30, 22, 14, 6, 61, 53, 45, 37,
                  29, 21, 13, 5, 28, 20, 12, 4]
"""Сокращение ключа с 64 до 56 бит"""

PBoxCompression = [14, 17, 11, 24, 1, 5, 3, 28,
                   15, 6, 21, 10, 23, 19, 12, 4,
                   26, 8, 16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55, 30, 40,
                   51, 45, 33, 48, 44, 49, 39, 56,
                   34, 53, 46, 42, 50, 36, 29, 32]
"""Сокращение ключа с 56 до 48 бит, получение раундового ключа"""

PBoxFinal = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]
"""Прямой P-бокс"""

PBoxExtention = [32, 1, 2, 3, 4, 5, 4, 5,
                 6, 7, 8, 9, 8, 9, 10, 11,
                 12, 13, 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21, 20, 21,
                 22, 23, 24, 25, 24, 25, 26, 27,
                 28, 29, 28, 29, 30, 31, 32, 1]
"""P-бокс расширения. Служит для расширения правой части текста до 48 бит"""

SBoxes = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
     ], [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ], [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ], [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ], [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ], [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ], [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ], [
         [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]
"""Таблица S-боксов"""

PlainText = open('text.txt', encoding='utf-8').read()
"""Открытый текст"""

Key = open('key.txt', encoding='utf-8').read()
"""Открытый ключ"""

BinaryText = ""
"""Текст в бинарном формате"""

BinaryKey = ''
"""Ключ в бинарном формате"""

LeftBinaryText = ''
"""Левая часть бинарного текста"""

RightBinaryText = ''
"""Правая часть бинарного текста"""

Permutation = ''
"""Вспомогательная переменная, участвующая при перестановках и XOR.
Значение изменяемой строки перезаписывается информацией из Permutation
"""

RoundKeys = []
"""Раундоовые ключи"""

EncodedText = ''
"""Зашифрованный текст"""

DesFunction = ''
"""Переменная, принимающая изменения в функции DES"""

'''ПОДГОТОВКА БИНАРНЫХ ТЕКСТА И КЛЮЧА'''
# перевод открытого текста в бинарный формат и начальная перестановка
for symbol in PlainText:
    BinarySymbol = bin(ord(symbol))[2:]
    while len(BinarySymbol) < 8:
        BinarySymbol = '0'+BinarySymbol
    BinaryText += BinarySymbol
while len(BinaryText) < 64:
    BinaryText = '00000000'+BinaryText
Permutation = ''
for i in InitialPermutation:
    Permutation += BinaryText[i-1]
BinaryText = Permutation

# перевод ключа в бинарный формат и сокращение до 56 бит
for symbol in Key:
    BinarySymbol = bin(ord(symbol))[2:]
    while len(BinarySymbol) < 8:
        BinarySymbol = '0'+BinarySymbol
    BinaryKey += BinarySymbol
while len(BinaryKey) < 64:
    BinaryKey = '00000000'+BinaryKey

# Сокращение ключа до 56 бит
Permutation = ''
for i in KeyPreparation:
    Permutation += BinaryKey[i-1]
BinaryKey = Permutation


'''СОЗДАНИЕ РАУНДОВЫХ КЛЮЧЕЙ'''
for i in range(16):
    Permutation = ''
    if i in [0, 1, 8, 15]:
        BitShift = BinaryKey[1:28]+BinaryKey[0] + \
            BinaryKey[29:]+BinaryKey[28]
        for j in PBoxCompression:
            Permutation += BitShift[j-1]
    else:
        BitShift = BinaryKey[2:28]+BinaryKey[0:2] + \
            BinaryKey[30:]+BinaryKey[28:30]
        for j in PBoxCompression:
            Permutation += BitShift[j-1]

    RoundKeys.append(Permutation)


'''АЛГОРИТМ ШИФРОВАНИЯ'''
for i in range(16):
    LeftBinaryText = BinaryText[:32]
    RightBinaryText = BinaryText[32:]

    '''ФУНКЦИЯ DES'''
    # расширение правой части текста
    Permutation = ''
    for j in PBoxExtention:
        Permutation += RightBinaryText[j-1]
    DesFunction = Permutation

    # XOR правой части текста и раундового ключа
    Permutation = ''
    for j in range(48):
        if DesFunction[j] == RoundKeys[i][j]:
            Permutation += '0'
        else:
            Permutation += '1'
    DesFunction = Permutation

    # Применяем S-боксы
    Permutation = ''
    for j in range(0, 48, 6):
        CurrentSBox = 0
        a = bin(SBoxes[CurrentSBox][int(DesFunction[j]+DesFunction[j+5], base=2)][int(
            DesFunction[j+1:j+5], base=2)])[2:]
        while len(a) < 4:
            a = '0'+a
        Permutation += a
        CurrentSBox += 1
    DesFunction = Permutation

    # Применяем прямой P-бокс
    Permutation = ''
    for j in PBoxFinal:
        Permutation += DesFunction[j-1]
    DesFunction = Permutation

    # XOR левой и правой части текста
    Permutation = ''
    for j in range(32):
        if LeftBinaryText[j] == RightBinaryText[j]:
            Permutation += '0'
        else:
            Permutation += '1'
    LeftBinaryText = Permutation
    # меняем местами правую и левую части текста
    BinaryText = RightBinaryText+LeftBinaryText
    if i == 15:
        BinaryText = BinaryText[32:]+BinaryText[:32]


# финальная перестановка
Permutation = ''
for i in FinalPermutation:
    Permutation += BinaryText[i-1]
BinaryText = Permutation

# получаем шифрованное собщение
for i in range(0, 64, 8):
    EncodedText += chr(int(BinaryText[i:i+8], base=2))
print(EncodedText)