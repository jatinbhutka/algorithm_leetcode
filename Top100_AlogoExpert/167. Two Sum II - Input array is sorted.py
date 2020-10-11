"""
We can apply Two Sum's solutions directly to get O(n^2)O(n2) time, O(1)O(1) space using brute force and O(n)O(n) time, O(n)O(n) space using hash table. 

However, both existing solutions do not make use of the property where the input array is sorted. We can do better.
"""


# Method 1: Use of input array is sorted Properties

# Time:O(N)
# Space: O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                return [i+1 , j+1]
            else:
                return -1
        
