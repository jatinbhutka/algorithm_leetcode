





"""
Approach #3 (Optimal) [Accepted]
The total number of operations of the previous approach is sub-optimal. For example, the array which has all (except last) leading zeroes: [0, 0, 0, ..., 0, 1].How many write operations to the array? For the previous approach, it writes 0's n-1n−1 times, which is not necessary. We could have instead written just once. How? ..... By only fixing the non-0 element,i.e., 1.

The optimal approach is again a subtle extension of above solution. A simple realization is if the current element is non-0, its' correct position can at best be it's current position or a position earlier. If it's the latter one, the current position will be eventually occupied by a non-0 ,or a 0, which lies at a index greater than 'cur' index. We fill the current position by 0 right away,so that unlike the previous solution, we don't need to come back here in next iteration.

In other words, the code will maintain the following invariant:
  1. All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
  2. All elements between the current and slow pointer are zeroes.
"""
# Method 2:

  #Time: O(N)
  #Space: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
                
        while j < len(nums):
            nums[j] = 0
            j += 1
            
        return nums
            
        
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i_non_zero = 0
        j_iter = 0
        while j_iter < len(nums):
            if nums[j_iter] != 0:
                nums[i_non_zero] = nums[j_iter]
                i_non_zero += 1
            j_iter += 1
        
        
        for i in range(i_non_zero, len(nums)):
            nums[i] = 0
        return nums

