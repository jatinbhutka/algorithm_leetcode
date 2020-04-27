"""
Brute Force Approch:
  For a Given problem you should try out all the possible solution and picked up desired solution.

Two types of Brute force approch:

  1. BackTracking: 
      - It is not for optimal solution (Like DP). It is use when you you have mutiple solution and you want all those solution.
      - It follows DFS
      

  2. Branch and Bound:
      - It follow BFS
    
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

        
