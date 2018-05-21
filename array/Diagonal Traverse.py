class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return ans
        m = len(matrix)
        n = len(matrix[0])
        c, r = 0, 0
        for i in range(0, m*n):
            ans.append(matrix[r][c])
            #####r+c 為偶數時往右上走
            if (r+c)%2 == 0:
                #####最右上邊的情況
                if c == n-1: r+=1
                ####在第一列但非最右之情況
                elif r == 0 : c+=1
                #####其餘狀況
                else:
                    c += 1
                    r -= 1
            #######r+c 為奇數時 往左下
            else:
                ###### 在最左下時
                if r == m-1: c+=1
                ###### 在地一行 但非最下
                elif c== 0: r+=1
                ##### 其餘
                else:
                    r +=1
                    c -=1
                    
        return ans
                    
