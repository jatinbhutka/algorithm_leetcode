# Method 1: : Linear Scan - Two pass

# Complexity Analysis

  # Time complexity : O(N) - This brute-force approach examines each of the n elements of nums exactly twice, so the overall runtime is linear.
  # Space complexity : O(1) - The linear scan method allocates a fixed-size array and a few integers, so it has a constant-size memory footprint.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break
        if first == -1:
            return [first, last]
        
        for i in range(len(nums)-1, -1,-1):
            if nums[i] == target:
                last = i
                break
 
        return [first, last]





# Method 2: Linear Scan - One pass

  # Time complexity : O(N) 
  # Space complexity : O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
  
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] != target:
                continue
            if first == -1:
                first = i
            last = i
        return [first, last]






# Method 1: : Modified Binary Search

# Complexity Analysis

  # Time complexity : O(Log N) - This brute-force approach examines each of the n elements of nums exactly twice, so the overall runtime is linear.
  # Space complexity : O(1) - The linear scan method allocates a fixed-size array and a few integers, so it has a constant-size memory footprint.
