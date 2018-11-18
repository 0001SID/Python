import os
board = {'1':'1','2':'2','3':'3',
         '4':'4','5':'5','6':'6',
         '7':'7','8':'8','9':'9'}
def print_board(board):
    print(' ',board['1'],' | ',board['2'],' | ',board['3'],' ')
    print('-----+-----+-----')
    print(' ',board['4'],' | ',board['5'],' | ',board['6'],' ')
    print('-----+-----+-----')
    print(' ',board['7'],' | ',board['8'],' | ',board['9'],' ')
    print('-----+-----+-----')
print('\n\t\t\t\tTIC-TAC-TOE\n\n')
print_board(board)
player = 1
turn = 'X'
for j in range(9):
    while True:
        print('\t\t\tPlayer ',player)
        position = input('Choose your position: ')
        if (board[position] == 'X' or board[position] == 'O'):
            print('Position already accupied')
        else:
            break
    board[position] = turn
    print_board(board)
    for i in range(1,10,3):
        if board[str(i)]==board[str(i+1)]==board[str(i+2)]:
            print('\t\t\tPlayer',player,'Win\n\t\t\t  Game Over')
            os._exit(0)
    for i in range(1,4):
        if board[str(i)]==board[str(i+3)]==board[str(i+6)]:
            print('\t\t\tPlayer',player,'Win\n\t\t\t  Game Over')
            os._exit(0)
    if board[str(1)]==board[str(5)]==board[str(9)]:
        print('\t\t\tPlayer',player,'Win\n\t\t\t  Game Over')
        os._exit(0)  
    if board[str(3)]==board[str(5)]==board[str(7)]:
        print('\t\t\tPlayer',player,'Win\n\t\t\t  Game Over')
        os._exit(0) 
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if player == 1:
        player = 2
    else:
        player = 1
    if j == 8:
        print('\n\t\t\tMatch tie no one win')