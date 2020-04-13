class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ret_l = []
        ret_r = []
        for ele in A:
            if ele%2 == 0:
                ret_l.append(ele)
            else:
                ret_r.append(ele)
        return ret_l+ret_r
        
# Time: O(N)
# Space: O(N)


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x%2 == 0] + [x for x in A if x%2 == 1])
        
# Time: O(N)
# Space: O(N)



class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        index = 0
        for i in range(len(A)):
            if A[i]%2 == 0:
                temp = A[index] 
                A[index] = A[i]
                A[i] = temp
                index += 1
        return A
        
# Time: O(N)
# Space: O(1)        
