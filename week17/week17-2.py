# week17-2.py
# LeetCode 1268. Search Suggestions System
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = defaultdict(list)
        for product in products:
            now = root
            for c in product:
                if c not in now:
                    now[c] = defaultdict(list)
                now = now[c]
            now["*"] = product
        now = root
        ans = []
        for c in searchWord:
            best = []
            if c not in now:
                noResult = len(searchWord) - len(ans)
                return ans + [[] for _ in range(noResult)]
            now = now[c]

            def helper(node):
                if "*" in node:
                    best.append(node["*"])
                for ch in node:
                    if len(best) < 3 and ch != "*":
                        helper(node[ch])
            helper(now)
            ans.append(best)
        return ans
