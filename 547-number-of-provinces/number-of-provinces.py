class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited =set()
        count = 0
        def fun(i,matrix) :
            if i<0 or i>=rows :
                return
            if (i) in visited :
                return False
            visited.add(i)
            for j in range(cols):
                if matrix[i][j] == 1:
                    fun(j,matrix)
            return True
        
        rows = len(isConnected)
        cols = rows
        for i in range(rows):
            if fun(i,isConnected) :
                count += 1
        return count

        