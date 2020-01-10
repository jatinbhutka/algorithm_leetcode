class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = curr_so_far = -float('inf')
        for i in range(len(nums)):
            curr_so_far += nums[i] # Add curr number
            curr_so_far = max(curr_so_far, nums[i]) # Check if should abandon accumulated value so far if it's a burden due to negative value accumulated
            max_so_far = max(max_so_far, curr_so_far) # Update answer
            
        return max_so_far
        
        
#Method 2: Divide and Conquer - Recursion:      
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def maxCrossingSum(arr, l, m, h) : 

            # Include elements on left of mid. 
            sm = 0; left_sum = -10000

            for i in range(m, l-1, -1) : 
                sm = sm + arr[i] 

                if (sm > left_sum) : 
                    left_sum = sm 


            # Include elements on right of mid 
            sm = 0; right_sum = -1000
            for i in range(m + 1, h + 1) : 
                sm = sm + arr[i] 

                if (sm > right_sum) : 
                    right_sum = sm 


            # Return sum of elements on left and right of mid 
            return left_sum + right_sum; 


        # Returns sum of maxium sum subarray in aa[l..h] 
        def maxSubArraySum(arr, l, h) : 

            # Base Case: Only one element 
            if (l == h) : 
                return arr[l] 

            # Find middle point 
            m = (l + h) // 2

            # Return maximum of following three possible cases 
            # a) Maximum subarray sum in left half 
            # b) Maximum subarray sum in right half 
            # c) Maximum subarray sum such that the 
            #	 subarray crosses the midpoint 
            return max(maxSubArraySum(arr, l, m), 
                    maxSubArraySum(arr, m+1, h), 
                    maxCrossingSum(arr, l, m, h)) 
        return maxSubArraySum(nums, 0, len(nums)-1)
        
