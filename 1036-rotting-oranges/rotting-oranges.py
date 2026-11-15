class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque
        queue = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1 :
                    count += 1
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            if count == 0:
                break
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        count -= 1
            minutes += 1
        return -1 if count > 0 else minutes
        