# Method 1: Pattern Iteratively

"""
nums = []
OUTPUT = [[]]
SIZE = 0 ||  OUTPUT SIZE = 1 = 2^0

nums = [1]
OUTPUT = [ [], [1]]
SIZE = 1 ||  OUTPUT SIZE = 2 = 2^1

nums = [1,2]
OUTPUT = [ [], [1], [2], [1,2]]
SIZE = 2, OUTPUT SIZE = 2 = 2^2

nums = [1,2,3]
OUTPUT = [ [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
SIZE = 3, OUTPUT SIZE = 8 = 2^3

nums = [1,2,3,4]
OUTPUT = [ [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3], [4], [1,4], [2,4], [1,2,4], [3,4], [1,3,4], [2,3,4], [1,2,3,4]]
SIZE = 4, OUTPUT SIZE = 16 = 2^4

For each new ele, OUTPUT array size increase by * 2.
So, We can Initiate empty list of list [[]].

and then we can iterate for each new element and add given element to each of the output element of previous iteration.

# Time:O(N X 2^N) 
# Space: O(N X 2^N) 

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        OUTPUT = [[]]
        
        for num in nums:
            OUTPUT += [lst + [num] for lst in OUTPUT]
        return OUTPUT
            

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        OUTPUT = [[]]
        
        for num in nums:
            new_OUTPUT = []
            for lst in OUTPUT:
                new_OUTPUT.append(lst+[num])
            OUTPUT = OUTPUT + new_OUTPUT
        return OUTPUT
        
        
        
"""
# Method2: DFS recursively

                                        []
                                     /   |  \
                                    /    |   \
                                   /     |    \
                                  /      |     \
                                 /       |      \
                              [1]       [2]     [3]
                             / \         |     
                            /   \        |      
                         [1,2]  [1,3]   [2,3]
                           /
                          /
                       [1,2,3]
                                    
"""        
