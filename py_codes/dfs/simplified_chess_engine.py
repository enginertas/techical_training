#!/usr/bin/env python

'''
Example Input:
3
2 1 1
N B 2
Q B 1
Q A 4
1 3 1
Q B 2
Q A 4
R A 3
B B 4
1 4 3
N D 1
Q A 4
R A 3
B B 4
B B 3

Example Output:
YES
NO
YES
'''

CHAR_START = 65
N_DIR = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]

def findNextSquares(board, move_list, row, col):
    squares = []
    for mv in move_list:
        if mv == "d":
            diag1, diag2 = False, False
            for k in reversed(range(0, row)):
                k2 = row - k
                if col - k2 >= 0 and not diag1:
                    squares.append((k, col - k2))
                    if board[k][col - k2] != '_':
                        diag1 = True     
                if col + k2 < 4 and not diag2:
                    squares.append((k, col + k2))
                    if board[k][col + k2] != '_':
                        diag2 = True
            diag1, diag2 = False, False
            for k in range(row + 1, 4):
                k2 = k - row
                if col - k2 >= 0 and not diag1:
                    squares.append((k, col - k2))
                    if board[k][col - k2] != '_':
                        diag1 = True     
                if col + k2 < 4 and not diag2:
                    squares.append((k, col + k2))
                    if board[k][col + k2] != '_':
                        diag2 = True    
        elif mv == "r":
            r_enc = False
            for k in reversed(range(0, col)):
                if not r_enc:
                    squares.append((row, k))
                    if board[row][k] != '_':
                        r_enc = True
            r_enc = False
            for k in range(col + 1, 4):
                if not r_enc:
                    squares.append((row, k))
                    if board[row][k] != '_':
                        r_enc = True                            
        elif mv == "c":
            c_enc = False
            for k in reversed(range(0, row)):
                if not c_enc:
                    squares.append((k, col))
                    if board[k][col] != '_':
                        c_enc = True
            c_enc = False
            for k in range(row + 1, 4):
                if not c_enc:
                    squares.append((k, col))
                    if board[k][col] != '_':
                        c_enc = True            
        elif mv == "n":
            for r, c in N_DIR:
                r, c = row + r, col + c
                if r >= 0  and r < 4 and c >= 0 and c < 4:
                    squares.append((r, c))
                    
    return squares
    
    
def findAvailableSquares(squares, cur_board, order):
    new_squares = []
    for i, j in squares:
        if order:
            if cur_board[i][j] == 'Q':
                return "FIN"   
            if ord(cur_board[i][j]) >= 97 and ord(cur_board[i][j]) <= 122:
                continue
        else:
            if cur_board[i][j] == 'q':
                return "FIN"
            if ord(cur_board[i][j]) >= 65 and ord(cur_board[i][j]) <= 90:
                continue
        new_squares.append((i, j))
    return new_squares
  
def copyBoard(old_board):
    new_board = [[], [], [], []]
    for i in xrange(4):
        for p in old_board[i]:
            new_board[i].append(p)   
    return new_board

def movePiece(board, i, j, sq):
    n_i, n_j = sq
    board[n_i][n_j] = board[i][j]
    board[i][j] = '_'
    
    
def findMoves(cur_board, order):
    next_boards = []
    for i in xrange(4):
        for j in xrange(4):
            squares = None
            if order:
                if cur_board[i][j] == 'q':
                    squares = findNextSquares(cur_board, ["d", "r", "c"], i, j)                    
                elif cur_board[i][j] == 'n':
                    squares = findNextSquares(cur_board, ["n"], i, j)                   
                elif cur_board[i][j] == 'b':
                    squares = findNextSquares(cur_board, ["d"], i, j) 
                elif cur_board[i][j] == 'r':
                    squares = findNextSquares(cur_board, ["r", "c"], i, j)
            else:
                if cur_board[i][j] == 'Q':
                    squares = findNextSquares(cur_board, ["d", "r", "c"], i, j)                    
                elif cur_board[i][j] == 'N':
                    squares = findNextSquares(cur_board, ["n"], i, j)                   
                elif cur_board[i][j] == 'B':
                    squares = findNextSquares(cur_board, ["d"], i, j) 
                elif cur_board[i][j] == 'R':
                    squares = findNextSquares(cur_board, ["r", "c"], i, j)                
            
            if squares:
                squares = findAvailableSquares(squares, cur_board, order)
                if squares == "FIN":
                    if order:
                        return "WIN"
                    else:
                        return "LOSS"
                for sq in squares:
                    n_b = copyBoard(cur_board)
                    movePiece(n_b, i, j, sq)
                    next_boards.append(n_b)

    return next_boards
    

def solve(cur_board, move_c, order):
    move_c -= 1
    if move_c < 0:
        return "NO" 
    
    possible_moves = findMoves(cur_board, order)
    if possible_moves == "WIN":
        return "YES"  
    if possible_moves == "LOSS":
        return "NO"
        
    if order:
        for p_m in possible_moves:
            soln = solve(p_m, move_c, not order)
            if soln == "YES":
                return "YES"
        return "NO"
    else:
        if_yes = "NO"
        for p_m in possible_moves:
            soln = solve(p_m, move_c, not order)
            if soln == "NO":
                return "NO"
            if soln == "YES":
                if_yes = "YES"
        
        return if_yes
   
    
def readInput():
    n_games = int(raw_input())
    for i in xrange(n_games):
        n_white, n_black, n_moves = map(int, raw_input().split())
        board = [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]
        for j in xrange(n_white):
            piece, col, row = raw_input().split()
            col = ord(col) - CHAR_START
            row = 4 - int(row)
            board[row][col] = piece.lower()
        for j in xrange(n_black):
            piece, col, row = raw_input().split()
            col = ord(col) - CHAR_START
            row = 4 - int(row)
            board[row][col] = piece
        print solve(board, n_moves, True)


if __name__ == "__main__":
    readInput()