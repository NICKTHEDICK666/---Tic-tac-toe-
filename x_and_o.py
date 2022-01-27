def privet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")



def show_matrix():
    print()
    print('    0   1   2   ')
    print('  -------------  ')
    for i, row in enumerate(matrix):
        row__ = f"{i} | {' | '.join(row)} | "
        print(row__)
        print('  -------------  ')
    print()




def ask():
    while True:
        x = int(input('Введите номер строки'))
        y = int(input('Введите номер столбца'))

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Неверный диапазон! ")
            continue

        if matrix[x][y] == " ":
            return x, y
        else:
            print('Клетка занята')
            continue


    return x, y

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(matrix[i][j])
        if symbols == ['x', 'x', 'x'] and ['o', 'o', 'o']:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(matrix[j][i])
        if symbols == ['x', 'x', 'x'] and ['o', 'o', 'o']:
            return True

    symbols = []
    for j in range(3):
        symbols.append(matrix[j][j])
    if symbols == ['x', 'x', 'x'] and ['o', 'o', 'o']:
        return True

    symbols = []
    for j in range(3):
        symbols.append(matrix[j][2-j])
    if symbols == ['x', 'x', 'x'] and ['o', 'o', 'o']:
        return True





privet()
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
count = 0
while True:
    count += 1
    show_matrix()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        matrix[x][y] = "x"
    else:
        matrix[x][y] = "o"


        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            break





