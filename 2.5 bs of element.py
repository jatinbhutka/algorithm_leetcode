# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:24:31 2019

@author: jatin
"""

# Python Program for recursive binary search.   
# Returns index of x in arr if present, else -1 

def search(arr, n, start, end):
    
    # Check base case
    if end >= start:
 
        mid = start + (end - start)//2 
        
        # If element is present at the middle itself 
        if arr[mid] == n:
            return mid
    
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > n:
            return search(arr, n, start , mid - 1 )
        
        # Else the element can only be present  
        # in right subarray 
        elif arr[mid] < n:
            return search(arr, n, mid + 1, end)

    else:
        # Element is not present in the array 
        return "Not present"



def binary_Search(arr, n):
    return search(arr, n, 0, len(arr) - 1)    


def main():
#   arr = [0, 1, 2, 3, 4, 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17]
    arr = [1, 3, 4, 6, 8, 9, 12, 14, 16, 17, 27, 33, 45, 51, 53, 63, 69, 70]
#    n = int(69)
    i = binary_Search(arr, 1)
    print("Index of : " + str(i)) 
    
main()
