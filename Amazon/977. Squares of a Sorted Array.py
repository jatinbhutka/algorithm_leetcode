class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        
        neg = -1
        for i in range(len(A)):
            if A[i] < 0:
                neg = i
                
        pos = neg + 1
        
        for i in range(len(A)):
            A[i] =  A[i] * A[i]
        
        i = 0
        ret = []
        while pos < len(A) and neg >= 0:
            if A[neg] <= A[pos]:
                ret.append(A[neg])
                neg -= 1
            elif A[pos] < A[neg]:
                ret.append(A[pos])
                pos += 1
        
        while pos < len(A):
            ret.append(A[pos])
            pos += 1
        while neg >= 0:
            ret.append(A[neg])
            neg -= 1  
        return ret
        
        
        
class Solution(object):
    def sortedSquares(self, A):
        # Time: O(N)
        # Space: O(N)    
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans        
        
