class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in dict:
                return dict[rem], i
            dict[num] = i
