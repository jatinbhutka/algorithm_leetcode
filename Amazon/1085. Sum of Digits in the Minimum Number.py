class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min = A[0]
        for ele in A:
            if ele < min:
                min = ele
        sum_dig = 0
        while min > 10:
            sum_dig += min%10
            min = min//10
        sum_dig += min
        
        if sum_dig%2 == 0:
            return 1
        else:
            return 0
            
            
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return (sum(int(x) for x in str(min(A))) % 2) ^ 1
        
        

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return (1- sum(int(x) for x in str(min(A)))%2)
        

class Solution:
	def sumOfDigits(self, A: List[int]) -> int:
		digit = str(min(A))
		res = 0
		for i in digit:
			res += int(i)
		if res % 2 != 0:
			return 0
		else:
			return 1
