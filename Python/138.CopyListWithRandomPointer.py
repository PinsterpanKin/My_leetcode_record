class MySolution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        old_to_new = {None: None}
    
    temp = head
    while temp:
        old_to_new[temp] = Node(temp.val)
        temp = temp.next
    
    temp = head
    while temp:
        clone = old_to_new[temp]
        clone.next = old_to_new[temp.next]
        clone.random = old_to_new[temp.random]
        temp = temp.next
        
    return old_to_new[head]

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        temp = head
        while temp:
            temp_copy = Node(temp.val, temp.next, None)
            temp.next = temp_copy
            temp = temp_copy.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        head_copy = head.next
        while temp:
            temp_copy = temp.next
            temp.next = temp_copy.next
            if temp_copy.next:
                temp_copy.next = temp_copy.next.next
            temp = temp.next
        return head_copy
