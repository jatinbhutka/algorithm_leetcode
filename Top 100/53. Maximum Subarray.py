
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
        
        



