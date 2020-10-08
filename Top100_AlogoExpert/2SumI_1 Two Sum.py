#### Brute Force:
# Time: O(n2)
# Space: O(1)


# Using Two Loop.

### Hashmap:
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Steps:
        # 1. Use hashMap: To store the visited element and Its Index
        # 2. Find Dif between Target and each given element.
        # 3. If Dif. in Hashmap. return Index of diff in hashmap and given ele index
        
        hashmap = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in hashmap:
                return [hashmap[dif], i]
            else:
                hashmap[num] = i

                
                
We can use this approach for any array if we sort it first, which bumps the time complexity to O(NlogN).

# Two Pointer Approch.

### Hashmap:
# Time: O(NLogN)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Steps:
        # 1. First Sort the array
        # 2. Use Two Pointer approach
    
        res = []
        numbers = [num for num in nums]
        numbers.sort()
        start_pointer = 0
        end_pointer = len(numbers) - 1
        while start_pointer < end_pointer:
            sum_of =  numbers[start_pointer] + numbers[end_pointer]
            if sum_of == target:
                first = numbers[start_pointer]
                second = numbers[end_pointer]
                break
            if sum_of > target:
                end_pointer -= 1
            else:
                start_pointer += 1
                
        for i in range(len(nums)):
            if first == nums[i] or second == nums[i]:
                res.append(i)
        return res
