class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while i < m and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]