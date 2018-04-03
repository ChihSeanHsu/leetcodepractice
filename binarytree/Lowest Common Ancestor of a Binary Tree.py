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
        if root == p or root == q or root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        
        if right and right:
           return root        
        return left if left else right
        
        
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if not root or root == p or root == q:
                return root
            elif self.isparent(p, q):
                return p
            elif self.isparent(q, p):
                return q
            elif self.isparent(root.left, q) and self.isparent(root.left, p):
                root = root.left
            elif self.isparent(root.right, q) and self.isparent(root.right, p):
                root = root.right
            else:
                break
        return root
        
    def isparent(self, p , c):
        if not p or p.val == None:
            return False
        if p == c:
            return True    
        return self.isparent(p.left, c) or self.isparent(p.right, c)
