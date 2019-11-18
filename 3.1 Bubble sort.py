# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:30:01 2019

@author: jatin
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def main():
    arr = [64, 34, 25, 12, 22, 11, 90] 
    a = bubbleSort(arr) 
    print ("Bubble Sorted array is:") 
    print (a)
main()


"""
https://www.geeksforgeeks.org/bubble-sort/

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.


Best: Î©(n)

Avg:Î˜(n^2)

Worst:O(n^2)

Auxiliary Space: O(1)



Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes

Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) 
in almost-sorted arrays and fix it with just linear complexity (2n). For example, it is used in a polygon filling algorithm, 
where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis) 
and with incrementing y their order changes (two elements are swapped) only at intersections of two lines (Source: Wikipedia)



"""
