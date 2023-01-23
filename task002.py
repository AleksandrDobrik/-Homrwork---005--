 
field = [[1,2,3],[4,5,6],[7,8,9]]
end = 0
player = True
count = 9


def check (field):
    end = 0
    for i in range(0,3):
        if field[i][0] == field[i][1] == field[i][2]:
            end = field[i][0]
    for j in range(0,3):
        if field[0][j] == field[1][j] == field[2][j]:
            end = field[0][j]
    if field[0][0] == field[1][1] == field[2][2]:
        end = field[1][1]
    if field[2][0] == field[1][1] == field[0][2]:
        end = field[1][1]
    return end


def print_field (field):
    for i in range(0,3):
        print('---------')
        for j in range(0,3):
            print(f'|{field[i][j]}|',end = '')
        print()
    print('---------')

while end == 0 and count != 0:
    print_field (field)
    count -= 1
    if player == True:
        n = int(input('Игрок X выберите свободную ячейку '))
        char = 'X'
    else:
        n = int(input('Игрок O выберите свободную ячейку '))
        char = 'O'
    if 4 > n > 0:
        field[0][n - 1] = char
    if 7 > n > 3:
        field[1][n - 4] = char
    if 10 > n > 6:
        field[2][n - 7] = char
    player = not player
    end = check (field)

if end == 0:
    print('ничья')
else:
    print(f'Выйграл игрок {end}')

    




