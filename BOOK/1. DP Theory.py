####

# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
# Dynamic Programming: 






"""
# Two Main Properties of DP Problem:

# 1. Overlapping Subproblem.
# 2. Optimal Substructure

1) Overlapping Subproblems:
##############################

Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again. For example, Binary Search doesn’t have common subproblems. If we take an example of following recursive program for Fibonacci Numbers, there are many subproblems which are solved again and again.

There are following two different ways to store the values so that these values can be reused:
a) Memoization (Top Down)
b) Tabulation (Bottom Up)

"""
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
  Both Tabulated and Memoized store the solutions of subproblems. In Memoized version, table is filled on demand while in Tabulated version, starting from the first entry, all entries are filled one by one. Unlike the Tabulated version, all entries of the lookup table are not necessarily filled in Memoized version. For example, Memoized solution of the LCS problem doesn’t necessarily fill all entries.

    Time taken by Recursion method is much more than the two Dynamic Programming 
    techniques mentioned above – Memoization and Tabulation!
"""





# 2. Optimal Substructure:
##############################
    
"""    
A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems.

For example, 
The Shortest Path problem has following optimal substructure property:
If a node x lies in the shortest path from a source node u to destination node v then the shortest path from u to v is combination of shortest path from u to x and shortest path from x to v. 

The standard All Pair Shortest Path algorithms like 
  1. Floyd–Warshall and 
  2. Bellman–Ford are typical examples of Dynamic Programming.

On the other hand, the Longest Path problem doesn’t have the Optimal Substructure property. 

Here by Longest Path we mean longest simple path (path without cycle) between two nodes. 

           Q   ---------> R
              <--------         
          | ^           | ^
          | |           | |
          | |           | |
          V |           V |
           S  ---------> T
              <--------
          


Consider the Above unweighted graph. There are two longest paths from q to t: q→r→t and q→s→t. Unlike shortest paths, these longest paths do not have the optimal substructure property. 

For example, the longest path q→r→t is not a combination of longest path from q to r and longest path from r to t, because the longest path from q to r is q→s→t→r and the longest path from r to t is r→q→s→t.


"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
