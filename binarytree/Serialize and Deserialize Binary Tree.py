# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def go(node):
            if node:
                res.append(str(node.val))
                go(node.left)
                go(node.right)
            else:
                res.append('n')
        res = []
        go(root)
        
        return ' '.join(res)
    

    def deserialize(self, data, node= None, layer = 0):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        def de_go():
            val = next(vals)
            if val == 'n':
                return None
            node = TreeNode(int(val))
            node.left = de_go()
            node.right = de_go()
            
            return node
            
            
        vals = iter(data.split())
        
        return de_go()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
