# Method 1: Recursive

class Solution:
    def isHappy(self, n: int) -> bool:
        
        h = []
        def check(n):

            l = [int(s) for s in str(n)]

            sum = 0 
            for dig in l:
                sum += dig*dig

            if sum == 1:
                return True

            if sum in h:
                return False

            h.append(sum)
            return check(sum)
        return (check(n))
        
        
#Method 2: Iterative
# ==================
def isHappy(self, n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1        
