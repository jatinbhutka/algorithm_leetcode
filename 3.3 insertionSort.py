# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:29:21 2019

@author: jatin
"""

def insertion_sortA (A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i - 1
        while (j>=0 and temp < A[j]):
            A[j+1]=A[j]
            j-=1
        A[j+1] = temp
    return A


def main():
    A = [64, 25, 12, 22, 11] 
    A = insertion_sortA(A)
    print ("Insertion Sorted array") 
    print(A)

main()

"""
Time Complexity	:            Space Complexity:
Best	Average	   Worst	    Worst

Î©(n)	Î˜(n^2)     	O(n^2)	    O(1)


Time Complexity: O(n*2)

Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
And it takes minimum time (Order of n) when elements are already sorted.

Algorithmic Paradigm: Incremental Approach

Sorting In Place: Yes

Stable: Yes

Online: Yes

Uses: Insertion sort is used when number of elements is small. 
It can also be useful when input array is almost sorted, only few elements are 
misplaced in complete big array.

"""
