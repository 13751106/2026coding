# week11-3.py
# LeetCode 700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root==None: return None
            if val < root.val:
                return helper(root.left, val)
            if val > root.val:
                return helper(root.right, val)
            if val == root.val:
                return root
        return helper(root, val)
