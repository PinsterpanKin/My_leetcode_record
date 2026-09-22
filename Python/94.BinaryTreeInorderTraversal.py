class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return res