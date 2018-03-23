# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
            
            
class Solution2:
    def go(self, root, res):
        if root:
            self.go(root.left, res)
            res.append(root.val)
            self.go(root.right, res)
    
        return res
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            res = []
            res = self.go(root, res)
            
        return res
