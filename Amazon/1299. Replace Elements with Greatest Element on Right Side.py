class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        large = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = large
            if temp > large:
                large = temp
        return arr
