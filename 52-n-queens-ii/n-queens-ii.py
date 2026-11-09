class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = []
        count = 0
        def isSafe(col):
            for r, c in enumerate(queens):
                if col == c :
                    return False
                if abs(r - len(queens)) == abs(c - col) :
                    return False
            return True

        def solve(current_row):
            nonlocal count
            if len(queens) == n:
                count += 1
                return
            for col in range(n):
                if isSafe(col) :
                    queens.append(col)
                    solve(current_row +1)
                    queens.pop()
        
        solve(0)
        return count
            