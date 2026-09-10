"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict = {}
        def fun(node) :
            if node in dict.keys() :
                return dict[node]
            if node is None:
                return
            node1 = Node(node.val)
            dict[node] = node1
            for neighbor in node.neighbors :
                node1.neighbors.append(fun(neighbor))
            return dict[node]
        return fun(node)
