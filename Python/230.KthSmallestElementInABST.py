class MySolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = 0

        def inorder(root: TreeNode) -> None:
            nonlocal k, res
            if not root:
                return
            inorder(root.left)
            if k > 0:
                k -= 1
                if k == 0:
                    res = root.val
                    return
            else:
                return
            inorder(root.right)

        inorder(root)
        return res

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right