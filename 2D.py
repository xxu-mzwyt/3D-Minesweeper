import random

board = []
display = []

board_size = 10
mine_num = 5

mine_cnt = 0

pos_list = [[ -1, -1], [ 0, -1], [ 1, -1],\
            [ -1,  0],           [ 1,  0],\
            [ -1,  1], [ 0,  1], [ 1,  1]]

def init():

    global mine_cnt

    for i in range(board_size):
        board.append([])
        display.append([])
        for j in range(board_size):
            board[i].append(0)
            display[i].append('#')

    def update_num(posx, posy):

        for item in pos_list:
            tarx = posx + item[0]
            tary = posy + item[1]
            if tarx >= 0 and tarx < board_size and tary >= 0 and tary < board_size:
                if board[tarx][tary] >= 0:
                    board[tarx][tary] += 1    

    while mine_cnt < mine_num:
        randx = random.randint(0, board_size-1)
        randy = random.randint(0, board_size-1)
        if board[randx][randy] != -1:
            board[randx][randy] = -1
            mine_cnt += 1
            update_num(randx, randy)

def show_display():

    for i in range(board_size):
        print()
        for j in range(board_size):
            print(display[i][j] + ' ', end='')
    print()

def play():

    def left_click(tarx, tary):

        global mine_cnt

        def reveal(posx, posy):

            display[posx][posy] = str(board[posx][posy])

            if board[posx][posy] > 0:
                return
            else:
                for item in pos_list:
                    tarx = posx + item[0]
                    tary = posy + item[1]
                    if tarx >= 0 and tarx < board_size and tary >= 0 and tary < board_size:
                        if display[tarx][tary] == '#':
                            reveal(tarx, tary)

        if display[tarx][tary] != '#':
            print("Error")
            return

        if board[tarx][tary] == -1:
            mine_cnt = -1
            return
        else:
            reveal(tarx, tary)

    def right_click(tarx, tary):

        global mine_cnt

        if display[tarx][tary] == '#':
            display[tarx][tary] = "*"
            if board[tarx][tary] == -1:
                mine_cnt -= 1

        elif display[tarx][tary] == '*':
            display[tarx][tary] = "#"
            if board[tarx][tary] == -1:
                mine_cnt += 1
        else:
            print("Error")
            return

    while mine_cnt > 0:
        show_display()
        comm = input().split(' ')
        if comm[0] == 'l':
            left_click(int(comm[1]), int(comm[2]))
        elif comm[0] == 'r':
            right_click(int(comm[1]), int(comm[2]))
        else:
            print("Error")

    if mine_cnt == 0:
        print("You win!")
    else:
        print("Boom!")

if __name__ == '__main__':
    init()

    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])

    play()
