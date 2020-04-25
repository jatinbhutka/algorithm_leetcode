
# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = float(-inf)
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_sum = max(nums[i], cur_sum)
            max_sum = max(cur_sum, max_sum)
            
        return max_sum
        
        

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
        
        



