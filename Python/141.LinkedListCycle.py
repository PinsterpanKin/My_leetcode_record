class MySolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        record = set() # or list, but set is faster for lookups
        while head:
            if head in record:
                return True
            record.add(head) # or record.append(head) if using list
            head = head.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False