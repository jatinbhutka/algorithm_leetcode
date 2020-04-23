
def isPalindrome(self, head):
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Steps:
            # 1. Find mid Using slow, fast pointer
            # 2. Reverse Half second half (Mid:)
            # 3. fast = head and compare slow and fast
        
        def rev_link (head):
            prev = None
            cur = head
            while (cur != None):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        slow = head
        fast = head
        
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            
        slow = rev_link(slow)
        fast = head
        
        while (slow is not None):
            if slow.val != fast.val:
                return False
            else:
                slow = slow.next
                fast = fast.next
        return True
            
        
        
        
        
