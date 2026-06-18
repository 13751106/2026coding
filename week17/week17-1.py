# week17-1.py
# LeetCode 208. Implement Trie (Prefix Tree)
class Trie:

    def __init__(self):
        self.root = defaultdict(list)

    def insert(self, word: str) -> None:
        now = self.root
        for c in word:
            if c not in now: now[c] = defaultdict(list)
            now = now[c]
        now['*'] = defaultdict(list)

    def search(self, word: str) -> bool:
        now = self.root
        for c in word:
            if c not in now: return False
            now = now[c]
        return '*' in now

    def startsWith(self, prefix: str) -> bool:
        now = self.root
        for c in prefix:
            if c not in now: return False
            now = now[c]
        return True
