# week13-5.py
# LeetCode 2542. Maximum Subsequence Score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)
        a = [(nums2[i], nums1[i]) for i in range(N)]

        a.sort(reverse=True)

        heap = [a[i][1] for i in range(k)]
        heapify(heap)
        total = sum(heap)
        ans = total * a[k-1][0]

        for i in range(k,len(nums2)):
            n2, n1 = a[i]
            heappush(heap, n1)
            total += n1 - heappop(heap)
            ans = max(ans, total*n2)
        return ans
