class MySolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_smaller(root, current_root):
            if not current_root:
                return True
            if current_root.val >= root.val:
                return False
            return is_smaller(root, current_root.left) and is_smaller(root, current_root.right)
        
        def is_bigger(root, current_root):
            if not current_root:
                return True
            if current_root.val <= root.val:
                return False
            return is_bigger(root, current_root.left) and is_bigger(root, current_root.right)
        
        if not root:
            return True
        if root.left and not is_smaller(root, root.left):
            return False
        if root.right and not is_bigger(root, root.right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

# Revised Solution with better performance
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)
