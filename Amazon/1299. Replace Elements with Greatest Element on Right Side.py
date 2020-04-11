class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        large = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = large
            if temp > large:
                large = temp
        return arr

    
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            l = arr[i+1]
            for j in range(i+1, len(arr)):
                if l<arr[j]:
                    l = arr[j]
            arr[i] = l
        arr[-1] = -1   
        return arr
    
    
#List Compri:

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = [max(arr[i+1:])for i in range(len(arr)-1)]
        k.append(-1)
        return k
