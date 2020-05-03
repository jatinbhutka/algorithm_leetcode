"""
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""


"""
Approach 3: Dynamic Programming
Steps:
Input: [10,9,2,5,3,7,101,18]
LIS :   [1,1,1,2,2,3,4,4]
longest increasing subsequence possible upto the ith index in a given array is independent of the elements coming later on in the array. Thus, if we know the length of the LIS upto ith index, we can figure out the length of the LIS possible by including the (i+1)th element based on the prev. element.
At the end, the maximum out of all the dp[i]s to determine the final result.
"""


# Time: O(N2) - Two loops of length n
# Space: O(N) - LIS array of size n

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        lis = [1]*n
        
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j] and lis[j] >= lis[i]:
                    lis[i] = lis[j] + 1
        return max(lis)
        
        
        

# Approach 4: Dynamic Programming with Binary Search 

# Time: O(NLogN) 
# Space: O(N) 


# Not Req. for Interview
