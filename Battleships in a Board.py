# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# Answer: 2
def countBattleships(self, board):

    ships = 0

    board = [['.' for i in board[0]]] + board + [['.' for i in board[0]]]
    for i in range(len(board)):
        board[i] = ['.'] + board[i] + ['.']

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                if board[i][j - 1] == 'O':
                    board[i][j] = 'O'
                    continue
                if board[i][j + 1] == 'O':
                    board[i][j] = 'O'
                    continue
                if board[i - 1][j] == 'O':
                    board[i][j] = 'O'
                    continue
                if board[i + 1][j] == 'O':
                    board[i][j] = 'O'
                    continue
                else:
                    ships += 1
                    board[i][j] = 'O'

    return ships

