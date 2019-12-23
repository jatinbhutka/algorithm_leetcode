"""

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = n = ListNode(0)
        rem = 0
        while l1 or l2 or rem:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = (val1 + val2 + rem)%10
            rem = (val1 + val2 + rem)//10
            n.next = ListNode(val)
            n = n.next
        return root.next
