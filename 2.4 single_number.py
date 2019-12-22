"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            
            if num not in nums[:i]+nums[i+1:]:
                return num
 # Time: O(n2)
 # Space: O(1)
 
 
 """
Approach 3: Math
Concept

2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c
 """
 class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (2 * sum(set(nums)) - sum(nums))
