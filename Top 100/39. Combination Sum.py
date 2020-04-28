"""
Brute Force Approch:
  For a Given problem you should try out all the possible solution and picked up desired solution.

Two types of Brute force approch:

  1. BackTracking: 
      - It is not for optimal solution (Like DP). It is use when you you have mutiple solution and you want all those solution.
      - It follows DFS
      

  2. Branch and Bound:
      - It follow BFS
      
Note: A greedy algorithm 
              is an algorithmic strategy that makes the best optimal choice at each small stage with the goal of this eventually leading to a globally optimum solution. This means that the algorithm picks the best solution at the moment without regard for consequences
    
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, index, path, ret):
            if target < 0:
                return
            if target == 0:
                ret.append(path)
                
            for i in range(index,len(nums)):
                dfs(nums, target-nums[i], i, path + [nums[i]], ret)
        
        ret = []
        candidates.sort()
        dfs(candidates, target, 0, [], ret)
        return ret

        

        
        
def combinationSum( candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs( nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        print(nums,"\t", target-nums[i], "\t", i,"\t", path+[nums[i]],"\t","Result:", res)
        dfs(nums, target-nums[i], i, path+[nums[i]], res)
        
        
candidates = [2,3,5]
target = 8
print(combinationSum(candidates,target))



# Steps: 

# BackTracking - DFS        
