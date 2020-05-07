## Simillar to Two sum problem:

# Time: O(N)
# Space: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff]+1, i+1]
            hashmap[num] = i
            
            
            
            


# Approch 2: Two Pointer
# Steps:
#   1. Use properties of sorted array to solve problem
#   2. 
#   3. 

eg1. numbers = [2,7,11,15] target=9
      i = 0, j=3 sum = 2+15 > 9 
      i = 0, j=2 sum = 2+11 > 9
      i = 0, j=1 sume = 2+7 == 9
      
      
      

# Time: O(N) - Each of the nn elements is visited at most once, thus the time complexity is O(n)O(n).
# Space: O(1) - We only use two indexes, the space complexity is O(1)O(1).

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0
        end_pointer = len(numbers) - 1
        while start_pointer < end_pointer:
            sum_of =  numbers[start_pointer] + numbers[end_pointer]
            if sum_of == target:
                return [start_pointer+1, end_pointer+1]
            if sum_of > target:
                end_pointer -= 1
            else:
                start_pointer += 1
                            
