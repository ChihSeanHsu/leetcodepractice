# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#######Bad way###########
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        elif len(preorder) ==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        top = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:top+1], inorder[:top])
        root.right = self.buildTree(preorder[top+1:], inorder[top+1:])
        
        
        
        return root
        
######nice way#######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        in_look={}
        for i, num in enumerate(inorder):
            in_look[num] = i
            
        return self.create_tree(in_look, preorder, inorder, 0, 0, len(inorder))
    
    def create_tree(self, lookup, preorder, inorder, prestart, instart, inend):
        if instart == inend :
            return None
        root = TreeNode(preorder[prestart])
        top = lookup[root.val]
        root.left = self.create_tree(lookup, preorder, inorder, prestart+1, instart, top)
        root.right = self.create_tree(lookup, preorder, inorder, prestart+top+1-instart, top+1, inend)
        
        return root
