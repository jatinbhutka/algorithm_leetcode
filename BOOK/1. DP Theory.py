####

# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
# Dynamic Programming: 


"""


                              
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)



"""






# 1. Top Down Approch -  Using Memorization


"""
 The memoized program for a problem is similar to the recursive version with a 
 small modification that it looks into a lookup table before computing solutions. 
 We initialize a lookup array with all initial values as NIL. Whenever 
 we need the solution to a subproblem, we first look into the lookup table. 
 If the precomputed value is there then we return that value, otherwise, 
 we calculate the value and put the result in the lookup table so that 
 it can be reused later.
"""
# Nth Fib:


n = 34
memo = [None] * (34+1)
memo[0] = 0
memo[1] = 1
def fib(n,memo):
    #print(memo)
    if memo[n]:
        return memo[n]
    if n == 0 or n == 1:
        return memo[n]
    else:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
        #print(memo)
        return memo[n]

print("FIb", fib(n,memo))





# Dynamic Programming: 
# 2. Bottom Up Approch - Tabulation

"""
The tabulated program for a given problem builds a table in bottom up fashion 
and returns the last entry from table. For example, for the same Fibonacci 
number, we first calculate fib(0) then fib(1) then fib(2) then fib(3) and 
so on. So literally, we are building the solutions of subproblems bottom-up.
"""

# Nth Fib:


def fibBU(n):
    lookup = [None] * (n+1)
    
    lookup[0] = 0
    lookup[1] = 1
    
    for i in range(2,n+1):
        if lookup[i]:
            return lookup[n]
        else:
            lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[n]
    

print(fibBU(n))
    
"""
    Time taken by Recursion method is much more than the two Dynamic Programming 
    techniques mentioned above – Memoization and Tabulation!
"""
    
    
    
