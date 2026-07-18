# Maximum Depth of Binary Tree 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
      """
        if not root :
            return 0
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))


# Balanced Binary Tree 
class Solution(object):
    def height(self,root):
        if not root:
            return 0
        left_depth = self.height(root.left)
        right_depth = self.height(root.right)
        return 1+ max(left_depth,right_depth)

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root :
            return True
        bal = self.height(root.left) - self.height(root.right)
        if (abs(bal) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)) :
            return True
        return False


# Diameter of Binary Tree 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(node):
		    if not node :
			    return 0
		    left = height(node.left)
		    right = height(node.right)
		
		    self.diameter = max(self.diameter , left + right)
		    return 1 + max(left , right)
        height(root)
        return self.diameter


# Binary Tree Level Order Traversal 
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = deque()
        result = []
        if not root :
            return result
        q.append(root)
        while q :
            l = []
            for i in range(len(q)) :
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(l)
        return result
        

# Invert Binary Tree - Beat 100%
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root :
            return root
        root.left , root.right  = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 


# Same Tree - 100%
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q :
            return True
        if not p :
            return False
        if not q :
            return False
        if p.val != q.val :
            return False
        left_val = self.isSameTree(p.left,q.left)
        right_val = self.isSameTree(p.right,q.right)
        return left_val and right_val


# Subtree of Another Tree 
class Solution(object):
    def isSameTree(self,root,subRoot) :
        if not root and not subRoot :
            return True
        if not root :
            return False
        if not subRoot :
            return False
        if root.val == subRoot.val :
            left_val = self.isSameTree(root.left,subRoot.left)
            right_val = self.isSameTree(root.right,subRoot.right)
            return left_val and right_val
        else:
            return False

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root and not subRoot :
            return True
        if not root:
            return False
        if not subRoot :
            return False
        if self.isSameTree(root,subRoot) :
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


# Lowest Common Ancestor of a Binary Search Tree 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val :
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val :
            return self.lowestCommonAncestor(root.right,p,q)
        else :
            return root

        
# Validate Binary Search Tree 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def Validate(node,min_val,max_val) :
            if not node :
                return True
            if node.val <= min_val or node.val >= max_val :
                return False
            return Validate(node.left,min_val,node.val) and Validate(node.right,node.val,max_val)
        
        return Validate(root,float('-inf'),float('inf'))


# Binary Tree Right Side View - Beat 100%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q = deque()
        result = []
        if not root :
            return result
        q.append(root)
        while q :
            level_size = len(q) 
            for i in range(level_size) :
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
                if i == level_size-1 :
                    result.append(node.val)
        return result


# Count Good Nodes in Binary Tree 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def validate(node,max_val) :
            if not node :
                return 0
            if node.val >= max_val :
                count = 1
            else :
                count = 0
            new_max = max(max_val , node.val)
            
            return count + validate(node.left,new_max) + validate(node.right, new_max)
        return validate(root,float('-inf'))
    
