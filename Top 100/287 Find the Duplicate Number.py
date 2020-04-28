
# Time: O(n^2)
# Space: O(1)

# 52/53 test cases pass. 1 Test  case failed

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i != j and nums[i] == nums[j]:
                    return nums[i]
                    


## Method 2: Sorting
# ===================
                            
# Time: O(nLOGn)
# Space: O(1) or O(n)
"""
Here, we sort nums in place, so the memory footprint is constant. If we cannot modify the input array, then we must allocate linear space for a copy of nums and sort that instead.
"""                 
                    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1
                            





## Method 3: Using Set()
#==========================


# Time complexity : O(n)
"""
Set in both Python and Java rely on underlying hash tables, so insertion and lookup have amortized constant time complexities. The algorithm is therefore linear, as it consists of a for loop that performs constant work nn times.
"""


# Space complexity: O(n)
""""
Algorithm

In order to achieve linear time complexity, we need to be able to insert elements into a data structure (and look them up) in constant time. A Set satisfies these constraints nicely, so we iterate over the array and insert each element into seen. Before inserting it, we check whether it is already there. If it is, then we found our duplicate, so we return it.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
                            



## Floyd's Tortoise and Hare (Cycle Detection)
# =============================================

"""
What happens when a fast runner (a hare) races a slow runner (a tortoise) on a circular track? At some point, the fast runner will catch up to the slow runner from behind.
"""

# Simillar to Question 142. Linked List Cycle II
# Time: O(N)
# Space: O(1) 


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
        

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]     
        return slow
