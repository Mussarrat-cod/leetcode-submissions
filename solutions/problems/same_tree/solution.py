class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both are empty
        if not p and not q:
            return True
        
        # Case 2: one is empty OR values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Case 3: check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))