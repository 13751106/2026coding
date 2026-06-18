# week17-4.py
# LeetCode 443. String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:
        N = 1
        prev, combo = chars[0], 0
        for c in chars:
            if c == prev: combo += 1
            else:
                if combo>1:
                    now = str(combo)
                    for c2 in now:
                        chars[N] = c2
                        N += 1
                prev, combo = c, 1
                chars[N] = c
                N += 1
        if combo > 1:
            now = str(combo)
            for c2 in now:
                chars[N] = c2
                N += 1
        return N
