# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_sum(self, root, suml, temp, sum):
        if root:
            temp += root.val
            suml = self.get_sum(root.left, suml, temp, sum)
            suml = self.get_sum(root.right, suml, temp, sum)
            
            if root.right==None and root.left==None:
                suml.append(temp)
        
        return suml
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        suml, temp = [] , 0
        suml = self.get_sum(root, suml, temp, sum)
        
        if sum in suml:
            return True
        
        return False
