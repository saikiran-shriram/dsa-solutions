"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {None: None}        
        dummy = head
        while dummy :
            visited[dummy] = Node(dummy.val)
            dummy = dummy.next
        node = head
        while node :
            visited[node].next = visited[node.next]
            if node.random:
                visited[node].random = visited[node.random]
            else:
                visited[node].random = None
            node = node.next
        return visited[head]
        