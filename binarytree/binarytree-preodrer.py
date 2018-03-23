# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visit = stack.pop()
            if root is None:
                continue
            elif is_visit:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
                
        return result
    
    
class Solution2:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return result
            root = stack.pop().right

        
