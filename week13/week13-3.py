# week13-3.py
# LeetCode 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)
