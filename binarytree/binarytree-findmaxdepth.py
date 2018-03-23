# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def go(self, root ,layer):
        if root:
            layer += 1
            l = self.go(root.left, layer)
            r = self.go(root.right, layer)
            layer = max(l,r)
            
            return layer
        else:
            return layer
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        layer = 0
        res = self.go(root, layer)
        
        return res     
        
        
        
class Solution2:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))     
