# week11-2.py
# LeetCode 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        def helper(root):
            count = 0
            if root==None: return 0
            if root==p or root==q: count += 1
            count += helper(root.left)
            count += helper(root.right)
            if count==2:
                a.append(root)
            return count
        helper(root)
        return a[0]
