# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p',
# and empty squares '.'.
#
# When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that
# direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white
# bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of
# available captures for the white rook is the number of pawns that the rook is attacking.
#
# Return the number of available captures for the white rook.
#
# Example 1:

# [[".",".",".",".",".",".",".","."],
#  [".",".",".","p",".",".",".","."],
#  [".","."p","B","R",".",".",".","p"],
#  [".",".",".",".",".",".",".","."],
#  [".",".",".",".",".",".",".","."],
#  [".",".",".","p",".",".",".","."],
#  [".",".",".",".",".",".",".","."],
#  [".",".",".",".",".",".",".","."]]
#
# Answer = 3

def numRookCaptures(self, board):
    result = 0

    n = 0
    s = 0
    e = 0
    w = 0

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == 'R':

                n_prime = -1
                s_prime = 1
                e_prime = 1
                w_prime = -1

                while n == 0:
                    if i + n_prime < 0:
                        n = 1
                        print('edge hit north')
                    else:
                        if board[i + n_prime][j] == "p":
                            n = 1
                            result += 1
                            print('pawn found north')
                        elif board[i + n_prime][j] == "B":
                            print('Bishop hit north')
                            n = 1
                        else:
                            n_prime += -1

                while s == 0:
                    if i + s_prime > len(board) - 1:
                        s = 1
                        print('edge hit south')
                    else:
                        if board[i + s_prime][j] == "p":
                            s = 1
                            result += 1
                            print('pawn found south')
                        elif board[i + s_prime][j] == "B":
                            print('Bishop hit south')
                            s = 1
                        else:
                            s_prime += 1

                while e == 0:
                    if j + e_prime > len(board[0]) - 1:
                        e = 1
                        print('edge hit east')
                    else:
                        if board[i][j + e_prime] == "p":
                            e = 1
                            result += 1
                            print('pawn found east')
                        elif board[i][j + e_prime] == "B":
                            print('Bishop hit east')
                            e = 1
                        else:
                            e_prime += 1

                while w == 0:
                    if j + w_prime < 0:
                        w = 1
                        print('edge hit west')
                    else:
                        if board[i][j + w_prime] == "p":
                            w = 1
                            result += 1
                            print('pawn found west')
                        elif board[i][j + w_prime] == "B":
                            w = 1
                            print('Bishop hit west')
                        else:
                            w_prime += -1

    return result
