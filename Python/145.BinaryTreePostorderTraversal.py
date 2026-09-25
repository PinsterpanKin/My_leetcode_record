class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def traverse(root: TreeNode):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)

        traverse(root)
        return res