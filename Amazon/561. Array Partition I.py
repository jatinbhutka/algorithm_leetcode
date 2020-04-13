class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
    # Time: N(Log N)
    # Space: O(1)
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_ += nums[i]
        return sum_        
