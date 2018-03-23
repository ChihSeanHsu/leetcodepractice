# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def go(self, root, dic, layer):
        if root:
            try:
                dic[layer].append(root.val)
            except:
                dic.append([])
                dic[layer].append(root.val)
            layer +=1
            dic = self.go(root.left, dic ,layer)
            dic = self.go(root.right, dic ,layer)
        
        return dic
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layer = 0
        dic = []
        res = self.go(root, dic, layer)
       
        
        
        return res
