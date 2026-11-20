class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom : 
            mid = (top + bottom) // 2
            if target < matrix[mid][0] :
                bottom = mid - 1
            elif target > matrix[mid][-1] :
                top = mid + 1
            else : 
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right :
                    mid_col = (left + right) // 2
                    if matrix[mid][mid_col] == target:
                        return True
                    elif matrix[mid][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1
                return False
        return False