class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #############################
        # Steps:
        #   1. Area = Side1 * side 2 [min of both side]
        #   2. Iterate over two loop.
        #   3. Area = (j-i) * min(a[i], a[j])
        #   4. Keep track on maximum are.
        ##############################
        
        
        # Time: O(N2)
        # Space: O(1)
        
        # 44 / 50 test cases passed.
        #==============================
        
        max_vol = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                vol = (j - i) * min(height[i], height[j])
                max_vol = max(max_vol, vol)
        return max_vol
        
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #############################
        # Steps:
        #   1. Start Two pointer. ith from front and jth from right(length(height) - 1)
        #   2. Move pointer of smaller heights towards greater heights
        #   3. Track maximum area.
        #   4.  
        #   5. 
        ##############################
        # Time: O(N)
        # Space: O(1)
        
        """
        The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
        """
        
        
        
        # Area will be maximum, when Width and height is maximum.
        # So, We will start with maximum width. (2 Pointer approch)
        # From Max width we will move towards, Maximum Heights.
        
        
        # Time: O(N2)
        # Space: O(1)
        
        max_area = 0
        i = 0
        j = len(height) - 1
        while i<j:
            if height[i] <= height[j]:
                max_area = max(max_area, height[i] * (j-i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j-i))
                j -= 1
        return max_area
                    
