class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def isSafe(r1,r2,c1,c2):
            if c1 == c2 :
                return False
            if abs(r1 - r2) == abs(c1 - c2) :
                return False
            return True  
        queens = []
        def solve(current_row): 
            if len(queens) == n :
                nonlocal count
                count += 1
                return
            for current_col in range(n): 
                safe = True
                for r, c in enumerate(queens):
                    if not isSafe(current_row, r, current_col, c):
                        safe = False
                        break
                if not safe:
                    continue
                queens.append(current_col)
                solve(current_row + 1)
                queens.pop()
        solve(0)
        return count
