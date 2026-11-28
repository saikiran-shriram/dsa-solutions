class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        max_area = 0
        def fun(grid,i,j) :
            if i<0 or i>=rows or j<0 or j>=cols :
                return 0
            if grid[i][j] == 0 :
                return 0
            if (i,j) in visited :
                return 0
            visited.add((i,j))
            area = 1
            area += fun(grid, i-1, j)
            area += fun(grid, i+1, j)
            area += fun(grid, i, j-1)
            area += fun(grid, i, j+1)
            return area 
        
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = fun(grid, i, j)
                    max_area = max(area, max_area)
        return max_area