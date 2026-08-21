class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def fun (grid,i,j,index) :
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False

            if grid[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            temp = grid[i][j]
            grid[i][j] = '#'

            if fun(grid, i + 1, j, index + 1):
                return True

            if fun(grid, i - 1, j, index + 1):
                return True

            if fun(grid, i, j + 1, index + 1):
                return True

            if fun(grid, i, j - 1, index + 1):
                return True

            grid[i][j] = temp

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if fun(board, i, j,0):
                    return True

        return False
        