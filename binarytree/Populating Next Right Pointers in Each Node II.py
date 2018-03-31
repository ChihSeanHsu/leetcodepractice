# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            p, q, nextN = root, None, None
            while p:
                if p.left:
                    if q: q.next = p.left
                    q = p.left
                    if nextN == None:
                        nextN = p.left
                if p.right:
                    if q: q.next = p.right
                    q = p.right
                    if nextN == None:
                        nextN = p.right
                    
                p = p.next
                
            self.connect(nextN)
                

class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left:  
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left:  
                        root.left.next = tmp.left
                        break
                    if tmp.right:
                        root.left.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left:  
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            #right need to be first    
            self.connect(root.right)
            self.connect(root.left)
