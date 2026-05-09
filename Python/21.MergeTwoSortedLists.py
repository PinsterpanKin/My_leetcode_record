# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=ListNode(0,None)
        temp=head
        while list1 and list2:
            if list1.val>=list2.val:
                temp.next=list2
                list2=list2.next
            else:
                temp.next=list1
                list1=list1.next
            temp=temp.next
        temp.next=list1 if list1 else list2
        return head.next