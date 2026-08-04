class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)     # Left
            result.append(node.val) # Root
            inorder(node.right)    # Right
        
        inorder(root)
        return result