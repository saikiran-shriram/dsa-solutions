class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def is_safe(row,col,queens):
            for prev_row in range(len(queens)) :
                prev_col = queens[prev_row]
                if col == prev_col :
                    return False
                if abs(row - prev_row) == abs(col - prev_col) :
                    return False
            return True
        queens = []
        def fun(row,queens) :
            nonlocal count
            if row ==n :
                count +=1 
                return 
            for col in range(n):
                if is_safe(row, col, queens):
                    queens.append(col)
                    fun(row + 1, queens)
                    queens.pop()
            return count
        return fun(0,queens)
