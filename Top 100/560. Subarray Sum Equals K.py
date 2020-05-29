# Method 2: Brute Force - Check for all possible Subarray.

# Time: O(N^2)
# Space: O(1)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum_c = 0
            for j in range(i, len(nums), 1):
                sum_c += nums[j]
                if sum_c == k:
                    count += 1   
        return count
        
        
        
        
        
# Method 2: 

# Time: O(N^2)
# Space: O(1)

       
