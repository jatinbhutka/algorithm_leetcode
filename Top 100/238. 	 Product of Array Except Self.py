
# Steps:
  # 1. element Output array = (Multiplication of all ele on right) * (Multiplication of all ele on left) 
  # 2. Iteration 1: Output array ele = (Multiplication of all ele on left) 
  # 3. Iteration 2: Output array ele = Output array ele * (Multiplication of all ele on right)
  # 4. Return Output
  

# Time: O(N)
# Space: O(1) Since, Output array does not count towards the space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [None] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]
            
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * right
            right *= nums[i]
        
        return output
        
        
        
# This takes,

# Time: O(N)
# Space: O(3n) Since, Output array does not count towards the space 

class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        ret_lef = [None] * len(a)
        ret_right = [None] * len(a)
        ret = [None] * len(a)

        left = 1
        ret_lef[0] = 1
        for i in range(1,len(a),1):
            ret_lef[i]  = left * a[i-1]
            left = ret_lef[i]
        print("\tLeft Multi:",ret_lef)

        right = 1
        ret_right[len(a)-1] = 1
        for i in range(len(a)-2, -1, -1):
            ret_right[i] = right * a[i+1]
            right = ret_right[i]

        print("\tRight multy:",ret_right)

        for i in range(len(a)):
            ret[i] = ret_right[i] * ret_lef[i]
        return ret
           
           
           
# This will not work, Since Some array contain 0 as well which will be issue.           
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Total_prod = 1
        for num in nums:
            Total_prod = Total_prod * num
            
        output = []
        for num in nums:
            ele = Total_prod//num
            output.append(ele)
        return output           
