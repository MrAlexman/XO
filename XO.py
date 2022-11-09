print("Hello, gamers! Choose who`s 'X' and who`s 'O'\n")

def your_turn(cell_num):
    file = open("XO.txt", "r")
    maket = ''.join(file.readlines())
    # return maket.format(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return maket.format(cell_num[0], cell_num[1], cell_num[2], cell_num[3], cell_num[4],
                        cell_num[5], cell_num[6], cell_num[7], cell_num[8], cell_num[9])


# print(your_turn([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

def winner(cell_num, who):
    poser = []
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 5, 3], [1, 5, 9]]
    for k, v in enumerate(cell_num):
        if v == who:
            poser.append(k)
    for i in win:
        # print(i)
        counter = 0
        for j in i:
            if j in poser:
                counter += 1
        if counter == 3:
            return True
    return False
yn = None
if __name__ == '__main__':
    while True:
        num_turn = 0
        cell = [0, '*', '*', '*', '*', '*', '*', '*', '*', '*']
        turns = set()
        print(your_turn(cell))
        while num_turn <= 8:
            turn = None
            if num_turn % 2 == 0:
                who = 'X'
            else:
                who = 'O'
            while turn not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Ввод числа от 1 до 9.")
                try:
                    turn = int(input(f"Введите номер ячейки. Ход {who}: "))
                except ValueError:
                    turn = None
                if turn not in turns:
                    turns.add(turn)
                else:
                    print("Не жульничай!")
                    turn = None
            cell[turn] = who
            print(your_turn(cell))
            if winner(cell, who):
                print(f"Побеза за {who}!")
                break
            num_turn += 1
        if num_turn == 9:
            print("Ничья!")
        print("Еще партию?")
        while yn not in ['y', 'n']:
            yn = None
            yn = input("Введите: (y/n)")
        if yn == 'n':
            break