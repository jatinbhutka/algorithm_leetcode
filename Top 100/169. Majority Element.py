# HashMap:        
# Time: O(N)
# Space: O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] += 1
        
        for key, val in h.items():
            if val > len(nums)//2:
                return key
            
   

# Sorting:
# Time: O(N Log N)
# Space: O(1)


# Here, If the majority element ever exit it will be at the middle of the array after sorting.
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]



# Moore Voting Algorithm:        
# Time: O(N)
# Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ind = 0
        count = 1
        for i in range(len(nums)):
            if nums[maj_ind] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_ind = i
                count = 1
        return nums[maj_ind]            
