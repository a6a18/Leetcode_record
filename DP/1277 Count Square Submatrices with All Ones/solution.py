class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        dp = []

        for _ in range(n):
            dp.append([0]*m)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
        
        count = 0

        for ii in range(n):
            for jj in range(m):
                count += dp[ii][jj]
        
        return count