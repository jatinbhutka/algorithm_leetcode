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

        # One Passs solution:
        # Steps:
        #   1. 
        #   2. 
        #   3. If temp < 1: 
        #   4. If temp > 1: 
        
        
"""
We are classifying the array into four groups: red, white, unclassified, and blue. Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. If the white pointer is blue, we swap with the latest unclassified element.
"""
# Time Complexity: O(N) 
# Space Complexity: O(1) 

"""
r w b
0 0 5
[2 1 0 1 2 0]

0 0 4
[0 1 0 1 2 2]

1 1 4
[0 1 0 1 2 2]

1 2 4
[0 1 0 1 2 2]

2 3 4
[0 0 1 1 2 2]

2 4 4
[0 0 1 1 2 2]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = len(nums)-1
        while w <= b:
            
            if nums[w] < 1:
                nums[w],nums[r] = nums[r], nums[w]
                w += 1
                r += 1     
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1

 
# Method 3:  No swap, no count  

        # One Passs solution:
        # Steps:
        #   1. Keep Two Pointer for 0 and 1
        #   2. Iterate through 0 to n:
        #       i. Store ele in temp.
        #       ii. Replace ele by 2.
        #       iii. If temp < 2: then ele_i = 1 Increase 1s pointer
        #       iv.  If temp == 0: then ele_j Increase os pointer
  
  
"""  
                  
[2 1 0 1 2 0]

0,0,0 --> 0,0,1
[2]

0,1,2
[2 2] --> [1 2]

0,2,2 --> 1,2,3
[1 2 2] ---> [1 1 2] ---> [0 1 2]

1,2,3 --> 1,3,4
[0 1 2 2] --> [0 1 1 2]

1,3,5
[0 1 1 2 2]

1,4,6 --> 2,4,6
[0 1 1 2 2 2] ---> [0 1 1 1 2 2] ---> [0 0 1 1 2 2]
  
"""
  
  
  
# Time Complexity: O(N) 
# Space Complexity: O(1) 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        for k in range(n):
            temp = nums[k]
            nums[k] = 2  
            if temp < 2:
                nums[j] = 1
                j += 1
            if temp == 0:
                nums[i] = 0
                i += 1  
                
                
                
