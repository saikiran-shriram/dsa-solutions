class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        total = 0
        for row in grid:
            row.sort()
        while grid[0]:  
            lst = []
            for row in grid:
                lst.append(row.pop())
            total += max(lst)
        return total
                