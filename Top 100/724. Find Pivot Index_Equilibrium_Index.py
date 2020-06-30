# Time : O(N)
# Space : O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            Total_sum -= nums[i]
            if Total_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
