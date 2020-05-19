# Brute Force: 187/202 Test Cases Passed.

# Time: O(n2)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)>1:
            max_global = float(-inf)
            for i in range(0, len(nums)):
                max_cur = nums[i]
                for j in range(i+1,len(nums)):
                    max_cur = max(nums[j], max_cur+nums[j])
                    max_global = max(max_cur, max_global)
            return max_global
        else:
            return nums[0]
        
        
# Method 2:    - 197/202 Test cases passed

# Time: O(N2)
# Space: O(N2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -2**31
        
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        max_sum = -float('inf')
        
        for i in range(n):
            dp[i][i] = nums[i]
        
        for i in range(n):
            for j in range(i, n):
                dp[i][j] = dp[i][j-1] + dp[j][j]
                max_sum = max(max_sum, dp[i][j])
                
        return max_sum        



# Time: O(n)
# Space: O(1)


# Kadane's Algo:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur = max_global = nums[0]
        for i in range(1, len(nums)):
            
            max_cur += nums[i]
            max_cur = max(nums[i], max_cur)
            max_global = max(max_cur, max_global)
            
        return max_global
        
        

# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
        
        



