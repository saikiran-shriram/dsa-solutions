class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        row = len(grid)
        col = len(grid[0]) 
        visited = set()
        r = 0
        c = 0
        last = [0,0]
        while r>=0 and r < row and c>=0 and c< col :
            if (r,c) in visited :
                return last
            visited.add((r,c))
            last = [r,c]
            if grid[r][c] == 'L' :
                c -= 1
            elif grid[r][c] == 'R' :
                c += 1
            elif grid[r][c] == 'U' :
                r -= 1
            else :
                r += 1
        return last 
