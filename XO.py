def your_turn (cell_num):
    file = open("XO.txt", "r")
    maket = ''.join(file.readlines())
    return maket.format(cell_num[0], cell_num[1], cell_num[2], cell_num[3],\
                        cell_num[4], cell_num[5], cell_num[6], cell_num[7], cell_num[8])

num_turn = 0
cell = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
while num_turn <= 8: #Здесь изменения
    turn = None
    if num_turn % 2 == 0:
        who = 'X'
    else:
        who = 'O'
    while turn not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        turn = int(input(f"Введите номер ячейки. Ход {who}: "))
    cell[turn] = who
    num_turn+=1



