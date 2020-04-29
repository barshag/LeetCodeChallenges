import  numpy as np
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        R = len(matrix)
        if (R>0):
            C = len(matrix[0])
        else:
            return 0
            
        dp = np.zeros((R,C))

        ret = 0
        for i in xrange(R):
            for j in xrange(C):
                if (matrix[i][j]=='1'):
                    dp[i][j] =1
                    if ((i>0) and (j>0)):
                        dp[i][j] += min (dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) 
                    ret = max(ret, dp[i][j])

        print(dp)
        return (int(ret**2))
        