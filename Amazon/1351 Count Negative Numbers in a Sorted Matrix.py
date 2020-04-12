class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
        return count
                
        
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(ele < 0 for i in grid for ele in i)
        
    
    
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(1 for j in grid for ele in j if ele<0)   
        

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        height = len(grid)
        h_lim = len(grid[0])
        result = 0
        i = 0
        j = 0
        while i < height:
            if j == h_lim and i < height:
                j = 0
                i += 1
            elif grid[i][j] >= 0:
                j += 1
            elif grid[i][j] < 0:
                result += 1
                j += 1 
        return result
        
        
        
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        res = 0
        i = j = 0
        while i < height :
            if j ==  width and i < height:
                j = 0
                i += 1
            elif grid[i][j] >= 0:
                j += 1
            elif grid[i][j] < 0:
                res += (height - i) * (width - j)
                width = j 
        return res     
