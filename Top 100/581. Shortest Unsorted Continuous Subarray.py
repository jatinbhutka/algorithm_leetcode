class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
         
        # Steps:
        # 1. Sort the given array and store in new_sorted
        # 2. Compare the ele by ele from front and back
        # 3. return dif
   
        
        # Time: O(NlogN)
        # Space: O(N)

        new_sorted =[ele for ele in nums]
        nums.sort()
        
        min_ind, max_ind = float(inf), float(-inf)
        for i in range(len(nums)):
            if new_sorted[i] != nums[i]:
                min_ind = min(min_ind, i)
                max_ind = max(max_ind, i)
                
        if max_ind - min_ind > 0:
            return max_ind - min_ind + 1
        else:
            return 0






class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        # Steps: https://www.youtube.com/watch?v=p-O7FExDH1M
        #   1. Find Min Value starting from (Start) Unsorted Array
        #   2. Find Max. Value starting from (end) Unsorted Array
        #   3. Find left_index the Place where we can place min Value
        #   4. Find right_index the place where we can place max value
        #   5. Return ( right_index -left_index + 1 ) if right_ind - left_ind > 0 else 0
        
        
        # Time: O(N)
        # Space: O(1)
        
        
        min_val = float(inf)
        max_val = float(-inf)
        
        flag = False
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                min_val = min(min_val, nums[i])
                
                
        flag = False
        for i in range(len(nums)-2, -1,-1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                max_val = max(max_val, nums[i])
                
        lf = 0
        rg = 0
        
        for lf in range(len(nums)):
            if min_val < nums[lf]:
                break
        
        for rg in range(len(nums)-1, -1,-1):
            if max_val > nums[rg]:
                break
                
        if rg - lf > 0:
            return (rg - lf)+1
        else:
            return 0
        
        
        
        
            
        
