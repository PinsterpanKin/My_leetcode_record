# Pay attention to the different types of ListNode and TreeNode.
class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        def find_middle(left, right):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convert_list_to_bst(left, right):
            if left == right:
                return None

            mid = find_middle(left, right)
            node = TreeNode(mid.val)

            node.left = convert_list_to_bst(left, mid)
            node.right = convert_list_to_bst(mid.next, right)

            return node

        return convert_list_to_bst(head, None)