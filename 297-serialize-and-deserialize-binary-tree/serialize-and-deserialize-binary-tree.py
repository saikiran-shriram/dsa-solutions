# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root :
            return ''
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node :
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else :
                result.append('null')
        while result[-1] == 'null':
            result.pop()
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q2 = deque()
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q2.append(root)
        i = 1
        while q2 :
            node = q2.popleft()
            if i < len(values):
                if values[i] != 'null' :
                    node.left = TreeNode(int(values[i]))
                else :
                    node.left = None
            i += 1
            if i < len(values):
                if values[i] != 'null' :
                    node.right = TreeNode(int(values[i]))
                else :
                    node.right = None
            i += 1
            if node.left:
                q2.append(node.left)
            if node.right :
                q2.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))