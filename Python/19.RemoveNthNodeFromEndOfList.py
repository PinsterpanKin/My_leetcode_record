"""
This problem showed me the data structure in Python
is somewhat different from what I fimiliar with in C++
OOP
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # move fast pointer n steps ahead
        for _ in range(n+1):
            fast = fast.next
            
        # move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # remove the nth node from the end
        slow.next = slow.next.next
        return dummy.next