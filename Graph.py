Number of Islands :
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def fun(grid, i, j):
            if i <0 or i >=len(grid) or j < 0 or j >=len(grid[0]) :
                return
            if grid[i][j] == '0' :
                return
            
            grid[i][j] = '0'

            fun(grid,i+1,j)
            fun(grid,i-1,j)
            fun(grid,i,j+1)
            fun(grid,i,j-1)
        
        count = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])):
                if grid[i][j] == '1' :
                    count +=1
                    fun(grid,i,j)
        return count

Clone Graph :
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        def fun(node):
            if not node :
                return None
            if node in visited :
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors :
                clone.neighbors.append(fun(neighbor))
            return clone
        return fun(node)


Course Schedule :
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()
        path = set()

        adj = {i :[] for i in range(numCourses)}
        for course,pre in prerequisites :
            adj[course].append(pre)
        def fun(node):
            if node in visited:
                return True
            if node in path :
                return False
            path.add(node)
            for neighbor in adj[node]:
                if not fun(neighbor):
                    return False
            path.remove(node)       
            visited.add(node)
            return True
        for i in range(numCourses):
            if not fun(i):
                return False
        return True
 

        