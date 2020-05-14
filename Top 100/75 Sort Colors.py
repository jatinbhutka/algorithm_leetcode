# Method 1: Two Pass

# Steps:
  # 1. First Pass: Count 0s,1s,2s.
  # 2. Second Pass: Replace value by counts till counts becomes 0.
  
# Time Complexity: O(N) - Two pass.
# Space Complexity: O(1) 


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two Passs solution:
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for num in nums :
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1
        
        for i in range(len(nums)):
            if count_0 > 0:
                nums[i] = 0
                count_0 -= 1
            elif count_1 > 0:
                nums[i] = 1
                count_1 -= 1
            else:
                nums[i] = 2
                count_2 -= 1

            
# Method 2: One Pass

# Steps:
  # 1. 
  # 2.
  # 3.
  
# Time Complexity: O(N) 
# Space Complexity: O(1)        
