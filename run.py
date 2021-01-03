import random

board = []
display = []

board_size = 5
mine_num = 10

mine_cnt = 0

pos_list = []


def on_board(x, y, z):

    if x < 0 or y < 0 or z < 0:
        return False
    if x >= board_size or y >= board_size or z >= board_size:
        return False
    return True 

def init():

    global mine_cnt

    for i in range(board_size):
        board.append([])
        display.append([])
        for j in range(board_size):
            board[i].append([])
            display[i].append([])
            for k in range(board_size):
                board[i][j].append(0)
                display[i][j].append('#')

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                pos_list.append([i, j, k])

    def update_num(posx, posy, posz):

        for item in pos_list:
            tarx = posx + item[0]
            tary = posy + item[1]
            tarz = posz + item[2]
            if on_board(tarx, tary, tarz) and board[tarx][tary][tarz] >= 0:
                board[tarx][tary][tarz] += 1    

    while mine_cnt < mine_num:
        randx = random.randint(0, board_size-1)
        randy = random.randint(0, board_size-1)
        randz = random.randint(0, board_size-1)
        if board[randx][randy][randz] != -1:
            board[randx][randy][randz] = -1
            mine_cnt += 1
            update_num(randx, randy, randz)

def show_display():

    for i in range(board_size):
        print("Layer" + str(i) + ":")
        for j in range(board_size):
            for k in range(board_size):
                print(display[i][j][k] + ' ', end='')
            print()
    print()

def play():

    def left_click(tarx, tary, tarz):

        global mine_cnt

        def reveal(posx, posy, posz):

            display[posx][posy][posz] = str(board[posx][posy][posz])

            if board[posx][posy][posz] > 0:
                return
            else:
                for item in pos_list:
                    tarx = posx + item[0]
                    tary = posy + item[1]
                    tarz = posz + item[2]
                    if on_board(tarx, tary, tarz) and display[tarx][tary][tarz] == '#':
                            reveal(tarx, tary, tarz)

        if display[tarx][tary][tarz] != '#':
            print("Error")
            return

        if board[tarx][tary][tarz] == -1:
            mine_cnt = -1
            return
        else:
            reveal(tarx, tary, tarz)

    def right_click(tarx, tary, tarz):

        global mine_cnt

        if display[tarx][tary][tarz] == '#':
            display[tarx][tary][tarz] = "*"
            if board[tarx][tary][tarz] == -1:
                mine_cnt -= 1

        elif display[tarx][tary][tarz] == '*':
            display[tarx][tary][tarz] = "#"
            if board[tarx][tary][tarz] == -1:
                mine_cnt += 1
        else:
            print("Error")
            return

    while mine_cnt > 0:
        show_display()
        comm = input().split(' ')
        if comm[0] == 'l':
            left_click(int(comm[1]), int(comm[2]), int(comm[3]))
        elif comm[0] == 'r':
            right_click(int(comm[1]), int(comm[2]), int(comm[3]))
        else:
            print("Error")

    if mine_cnt == 0:
        print("You win!")
    else:
        print("Boom!")

if __name__ == '__main__':
    
    init()
    play()
