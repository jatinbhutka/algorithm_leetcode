""""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

"""

# Method 1:
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 1
        while A[i] >A[i - 1]:
            if A[i] > A[i+1]:
                return i
            i += 1
        
        
# Method 2:

class Solution:
    def peakIndexInMountainArray(self, A):

        #mountain = -1
        
        for i in range(len(A)-1): # given that array will be mountain,  
            if A[i] > A[i+1]:     # hence just looking for A[i] > A[i+1]
                return i
                
                
#Method 3: Binary search tree

def peakIndexInMountainArray(self, A: List[int]) -> int:
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if A[mid-1] < A[mid]:
            start = mid
        else:
            end = mid
    if A[start] < A[end]:
        return end
    return start
