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
