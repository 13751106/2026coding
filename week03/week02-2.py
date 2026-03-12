# week02-2.py
# LeetCode 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        total = sum( nums[:k] )
        maxTotal = total
        for i in range(k, N):
            total = total + nums[i] - nums[i-k]
            maxTotal = max(maxTotal, total)
        return maxTotal / k
