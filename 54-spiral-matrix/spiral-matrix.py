class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) -1 
        while top <= bottom and left <= right:
            column = left
            while column <= right:
                result.append(matrix[top][column])
                column += 1
            top += 1
            row = top
            while row <= bottom :
                result.append(matrix[row][right])
                row += 1
            right -= 1 
            if top <= bottom :
                column = right
                while column >= left :
                    result.append(matrix[bottom][column])
                    column -= 1
                bottom -= 1
            if left <= right :
                row = bottom
                while row >= top :
                    result.append(matrix[row][left])
                    row -= 1
                left += 1
        return result