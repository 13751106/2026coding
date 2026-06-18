# week17-3.py
# LeetCode 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        V = "aeiouAEIOU"
        stack = []
        for c in s:
            if c in V: stack.append(c)

        ans = ""
        for c in s:
            if c in V: ans += stack.pop()
            else: ans += c
        return ans
