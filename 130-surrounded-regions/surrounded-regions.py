class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0]) 
        def fun(r,c) :
            if r <0 or r >= row or c <0 or c >= col :
                return
            if board[r][c] != 'O':
                return
            board[r][c] = 'S'
            fun(r + 1, c)
            fun(r - 1, c)
            fun(r, c + 1)
            fun(r, c - 1)
            return True
        for j in range(col) :
            fun(0,j) 
            fun(row-1,j)
        for i in range(row) :
            fun(i,0)
            fun(i,col-1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'



