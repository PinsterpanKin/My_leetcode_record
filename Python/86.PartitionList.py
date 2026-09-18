class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        small_head = ListNode(0)
        small = small_head
        large_head = ListNode(0)
        large = large_head
        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next
            current = current.next
        large.next = None
        small.next = large_head.next
        return small_head.next