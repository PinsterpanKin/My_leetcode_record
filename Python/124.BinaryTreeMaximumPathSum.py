class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            current_max_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_max_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum