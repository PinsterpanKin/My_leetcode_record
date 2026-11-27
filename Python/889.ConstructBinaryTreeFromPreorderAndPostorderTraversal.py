class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        left_val = preorder[1]
        left_size = postorder.index(left_val) + 1
        
        root.left = self.constructFromPrePost(preorder[1:left_size + 1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size + 1:], postorder[left_size:-1])
        
        return root