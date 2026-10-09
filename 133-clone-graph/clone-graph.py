"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}  
        def fun(node):
            if node in visited:
                return visited[node]
            if node is None:
                return
            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(fun(neighbor))
            return clone
        return fun(node)