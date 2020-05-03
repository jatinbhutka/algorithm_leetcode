# Approach 2: Dynamic Programming 2D


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Time: O(MN)
        # Space: O(MN)
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [ [ None for c in range(col) ] for r in range(row) ] 
        
        dp[0][0] = grid[0][0]
        
        for i in range(1,n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for j in range(1,m):
            dp[j][0] = grid[j][0] + dp[j-1][0]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
                
        return dp[m-1][n-1]


# Approach 3: Dynamic Programming 1D

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Time: O(MN) - We traverse the entire matrix once.
        # Space: O(N) - Another array of row size is used.
        
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [None] * cols
        dp[0] = grid[0][0]
        
        for c in range(1,cols):
            dp[c] = dp[c-1] + grid[0][c]
            
        for r in range(1, rows):
            for c in range(cols):
                if c == 0:
                    dp[0] += grid[r][c]
                else:
                    dp[c] = grid[r][c] + min(dp[c-1], dp[c])
        return dp[cols-1]


# Approach 4: Dynamic Programming (Without Extra Space):
"""
 Instead of using another dpdp matrix. We can store the minimum sums in the original matrix itself, since we need not retain the original matrix here
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Time: O(MN) - We traverse the entire matrix once.
        # Space: O(1) - No extra space is used.
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1,n):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        
        for j in range(1,m):
            grid[j][0] = grid[j][0] + grid[j-1][0]
   
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
                
        return grid[m-1][n-1]

       
