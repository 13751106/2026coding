# week11-5.py
# LeetCode 199. Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, level):
            if root==None: return
            if len(ans) <= level:
                ans.append( root.val )
            else:
                ans[level] = root.val
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return ans
