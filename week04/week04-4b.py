# week04-4b.py
# LeetCode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums:
            H[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1:
                return nn
        return -1
