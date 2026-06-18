# week17-5.py
# LeetCode 1161. Maximum Level Sum of a Binary Tree
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = []
        def helper(root, level):
            if root==None: return
            if level >= len(levelSum): levelSum.append(0)
            levelSum[level] += root.val
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        M = max(levelSum)
        return levelSum.index(M) + 1
