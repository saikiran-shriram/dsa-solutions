class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def fun(i,j,grid) :
            if i <0 or i>= rows or j <0 or j>= cols :
                return False
            if grid[i][j] == '0' :
                return False
            if (i,j) in visited :
                return False
            visited.add((i,j))

            fun(i+1,j,grid)
            fun(i,j+1,grid)
            fun(i-1,j,grid)
            fun(i,j-1,grid)
            return True

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows) :
            for j in range(cols) :
                if fun(i,j,grid) :
                    count += 1
        return count