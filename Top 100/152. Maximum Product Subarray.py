class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #min can turn max when encountering another negative number
        #so we have to record all the min and max values
        
        #we need two variables to record the previous min and max products and
        #final_max to store the actual max
        
        
        
        # Thought Process: Immeditly
        
        #   1. What Are possible sub-array.
        #   2. Track product
        #   3. find Max of all
        
        # Two method for Brute Force:
        
        # 1. A: O(N^3)
        
        
        
        # 2. A: O(N^2)
        
        
        
        # B: 
        
        # Time: O(N)
        # Space: O(1)
        
        # Simmilar to Max Subarray problem. (53. Maximum Subarray.py)
        # https://github.com/jatinbhutka/algorithm_leetcode/blob/master/Top%20100/53.%20Maximum%20Subarray.py
        
        curr_max = nums[0]
        curr_min = nums[0]
        final_max = nums[0]
        
        for i in range(1,len(nums)):
            temp = curr_max
            curr_max = max(max(curr_max*nums[i],curr_min * nums[i]),nums[i])
            curr_min = min(nums[i],min(curr_min*nums[i],temp * nums[i]))
            final_max = max(curr_max,final_max)
            
        return final_max
