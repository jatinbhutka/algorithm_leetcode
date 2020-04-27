class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Steps:
        # 1. Transpose Matrix
        # 2. Reverse each list
        
        # Time complexity : O(N^2)
        # Space complexity : O(1) since we do a rotation in place.

        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix
        
