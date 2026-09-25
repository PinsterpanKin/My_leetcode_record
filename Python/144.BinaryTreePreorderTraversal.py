class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def traverse(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return res
