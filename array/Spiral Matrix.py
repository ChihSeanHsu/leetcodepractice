class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix or not matrix[0]: return ans
        r = len(matrix[0]) #right-edge
        d = len(matrix) # down-edge
        u, l =0, 0 #up-edge & left-edge
        while(True):
            #do upper
            for col in range(l, r):
                ans.append(matrix[u][col])
            u += 1
            if (u == d): break
            # do right
            for row in range(u, d):
                ans.append(matrix[row][r-1])#list index r-1
            r -= 1
            if (r == l): break
            # do down
            for col in range(r-1, l-1, -1):
                ans.append(matrix[d-1][col])
            d -= 1
            if (d == u):break
            # do left
            for row in range(d-1, u-1, -1):
                ans.append(matrix[row][l])
            l += 1
            if (l==r): break
            
        return ans
            
