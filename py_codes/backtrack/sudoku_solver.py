#!/usr/bin/env python

class Solution(object):
    def __init__(self):
        self._row_bitmap = [0] * 9
        self._col_bitmap = [0] * 9
        self._box_bitmap = [[0 for j in xrange(3)] for i in xrange(3)]
        
    
    def _setSquare(self, row, col, val, set_on_board = False):
        self._row_bitmap[row] |= (1 << val)
        self._col_bitmap[col] |= (1 << val)
        self._box_bitmap[row/3][col/3] |= (1 << val)
        if set_on_board:
            self._board[row][col] = chr(val + 49)

    
    def _clearSquare(self, row, col, val):
        if val < 0:
            return 
        self._row_bitmap[row] &= ~(1 << val)
        self._col_bitmap[col] &= ~(1 << val)
        self._box_bitmap[row/3][col/3] &= ~(1 << val)
       
    
    def _getTotalBitmap(self, row, col):
        return self._row_bitmap[row] | self._col_bitmap[col] | self._box_bitmap[row/3][col/3]
            
        
    def _getSetBitCount(self, row, col):
        total_bitmap = self._getTotalBitmap(row, col)
        set_bit_count = 0
        while total_bitmap > 0:
            if total_bitmap & 1 == 1:
                set_bit_count += 1
            total_bitmap >>= 1
        return set_bit_count
        
        
    def _getNextAvailableValue(self, row, col, val):
        total_bitmap = self._getTotalBitmap(row, col)
        if total_bitmap == 0x1ff:
            return -1
        
        val += 1
        while val < 9 and total_bitmap & (1 << val) > 0:
            val += 1
            
        if val == 9:
            return -1
        
        return val
        
        
    def solveSudoku(self, board):
        self._board = board
        
        empty_squares = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    empty_squares.append([i, j, -1])
                else:
                    self._setSquare(i, j, ord(board[i][j]) - 49)
                    
        empty_squares.sort(key=lambda x: self._getSetBitCount(x[0], x[1]), reverse=True)
     
        square_i = 0
        while square_i < len(empty_squares):
            row, col, prev_val = empty_squares[square_i]
            self._clearSquare(row, col, prev_val)
            next_val = self._getNextAvailableValue(row, col, prev_val)
            if next_val == -1:
                empty_squares[square_i][2] = -1
                square_i -= 1
            else:
                self._setSquare(row, col, next_val, True)
                empty_squares[square_i][2] = next_val
                square_i += 1
                        
            
if __name__ == "__main__":
    test = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    for i in xrange(len(test)):
        test[i] = list(test[i])

    Solution().solveSudoku(test)
    
    for i in xrange(len(test)):
        test[i] = ''.join(test[i])
        print test[i]