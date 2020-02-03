import numpy as np
import sys

def put_stone(board, turn, player):
    """
    Checking if place available and putting stone there.

    :param board:
    :param turn:
    :param player:
    :return: board, check_turn
    """
    check_turn = False

    for i in range(cols_num):
        if board[rows_num - 1 - i][turn] == 0:
            board[rows_num - 1 - i][turn] = player
            check_turn = True
            break

    if check_turn == False:
        print('You cannot put stone instead other stone')

    return board, check_turn

def input_handler():
    """
    Input handler for checking players input between their turns
    :return: turn
    """
    while(True):
        try:
            turn = int(input())

            if turn in range(1,cols_num+1):
                break
            else:
                raise Exception("Invalid column! ")
        except:
            print('Please, input a correct column  in range 1-{}'.format(board.shape[1]))

    return turn

def check_list(row):
    """
    Checking list for same consecutive values

    :param row:
    :return: num of player
    """
    counter = 0
    winner = None

    for i in range(len(row)):
        if row[i]== 0:
            continue

        if i == (len(row)-1):
            break

        if row[i] == row[i+1]:
            counter += 1
            winner = row[i]
        else:
            counter = 0
            winner = None

        if counter == 3:
            return winner

    return None

def check_winner(board):
    """
    Checking board for winner
    My idea is to convert all rows, columns and diag's to 1-d array, and check with function check_list
    :param board:
    """

    # For rows
    for i in range(rows_num):
        row = board[i,:]
        winner = check_list(row)

        if winner is not None:
            print('Winner is player {}'.format(winner))
            sys.exit()

    # For columns
    for i in range(cols_num):
        column = board[:,i]
        winner = check_list(column)

        if winner is not None:
            print('Winner is player {}'.format(winner))
            sys.exit()

    # For diagonals
    # get diags from left side
    diags = [board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])]
    # get diags from right side
    diags.extend(board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1))

    for i in range(len(diags)):
        if len(diags[i]) >= 4:
            column = diags[i]
            winner = check_list(column)

            if winner is not None:
                print('Winner is player {}'.format(winner))
                sys.exit()

def print_board(board):
    """
    Function for printing 2-d array without brackets
    :param board:
    """
    for a in board:
        for elem in a:
            print("{}".format(elem).rjust(3), end="")
        print(end="\n")

def player_turn(board, player_num):
    """
    Turn function for selected player
    :param board:
    :param player_num:
    :return: board
    """
    print('Player {} turn'.format(player_num + 1))
    turn = input_handler()
    board, check_turn = put_stone(board, turn - 1, player_num + 1)
    print_board(board)

    if check_turn == False:
        player_turn(board, player_num)
    else:
        return board

def input_configs():
    """
    For checking  configs
    :return:
    """
    print("Please, input number of columns")
    columns = int(input())
    print("Please, input number of rows")
    rows = int(input())
    print('Please, input number of players')
    players = int(input())
    return columns, rows, players

if __name__ == '__main__':
    # loop for configs
    while(True):
        try:
            cols_num, rows_num, players_num = input_configs()
            if cols_num <= 3 or rows_num <=3 or players_num <= 1:
                print('Input correct configs')
            else:
                break
        except:
            print('Input correct configs!!')

    print('Choose num of column, where you wan to put your stone')

    board_size = (rows_num, cols_num)
    players_num = players_num
    # Creating numpy array with selected size
    board = np.zeros(board_size).astype('int64')

    print_board(board)

    # loop for game
    while(True):
        for i in range(players_num):
            if board is not None:
                check_winner(board)
                board = player_turn(board,i)