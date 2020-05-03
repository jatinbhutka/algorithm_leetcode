class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1,n) + self.uniquePaths(m, n-1)
        
 
# Approach 1: Dynamic Programming:

# Steps:
  # 1. Initialize 2-D Array of size m * n with all elemenet = 1
  # 2. For any given Inner cells, 
      # position = No. of ways = Ways for above position + ways for left cell
  # 3. Return dp[m-1][n-1]
  
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Time complexity: O(N×M)
        # Space complexity: O(N×M)
        
        dp = [[1 for col in range(n)] for row in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]
                
        


