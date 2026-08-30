class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                new_i = j                 
                new_j = len(matrix)-1-i
                temp = matrix[j][len(matrix)-1-i]
                matrix[new_i][new_j] = matrix[i][j]
                temp1 = matrix[new_j][len(matrix)-1-j]
                matrix[new_j][len(matrix)-1-j] = temp
                temp2 = matrix[len(matrix)-1-j][i]
                matrix[len(matrix)-1-j][i] = temp1
                matrix[i][j] = temp2


        