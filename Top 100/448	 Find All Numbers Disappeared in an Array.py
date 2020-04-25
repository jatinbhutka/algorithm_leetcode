
# Time: O(N)
# Space: O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])
    
        ret = []
        for i, num in enumerate(nums):
            if num > 0:
                ret.append(i+1)
        return ret
