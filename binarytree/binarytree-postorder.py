# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def go(self, root, temp):
        if root:
            self.go(root.left, temp)
            self.go(root.right, temp)
            temp.append(root.val)
        
        return temp
    
    
    def postorderTraversal(self, root):
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
            
            
 
