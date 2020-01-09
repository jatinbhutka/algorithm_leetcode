'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s = None     
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 and l2:

            if l1.val <= l2.val:
                s = l1                
                l1 = l1.next
            else:
                s = l2
                l2 = l2.next
            new_head = s

        while l1 and l2:
            if l1.val <= l2.val:
                s.next = l1
                s = l1
                l1 = l1.next
            else:
                s.next = l2
                s = l2
                l2 = l2.next
        if not l1:
            s.next = l2
        else:
            s.next = l1
            
        return new_head

    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Method 2:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            newhead = l1
            l1 = l1.next
        else:
            newhead = l2
            l2 = l2.next
        rethead = newhead
        
        while l1 and l2:
            if l1.val <= l2.val:
                newhead.next = l1
                l1 = l1.next
            else:
                newhead.next = l2
                l2 = l2.next
            newhead = newhead.next
        if l1:
            newhead.next = l1
        else:
            newhead.next = l2
        return rethead
    
    
# Method 3:

# Method 2:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            newhead = l1
            l1 = l1.next
        else:
            newhead = l2
            l2 = l2.next
        rethead = newhead
        
        while l1 and l2:
            if l1.val <= l2.val:
                newhead.next = l1
                l1 = l1.next
            else:
                newhead.next = l2
                l2 = l2.next
            newhead = newhead.next
            
        newhead.next = l1 if l1 is not None else l2
        return rethead
    
    
# Method 4:
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
