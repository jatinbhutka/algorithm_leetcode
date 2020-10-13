"""
Before jumping in, let's check the existing solutions and determine the best conceivable runtime (BCR) for 3Sum:

Two Sum uses a hashmap to find complement values, and therefore achieves \mathcal{O}(N)O(N) time complexity.
Two Sum II uses the two pointers pattern and also has \mathcal{O}(N)O(N) time complexity for a sorted array. We can use this approach for any array if we sort it first, which bumps the time complexity to \mathcal{O}(n\log{n})O(nlogn).
Considering that there is one more dimension in 3Sum, it sounds reasonable to shoot for \mathcal{O}(n^2)O(n 
2
 ) time complexity as our BCR.

"""

Time Complexity: O(N2)
Space Complexity: O(N)

# Method 1: Two Pointers



class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
