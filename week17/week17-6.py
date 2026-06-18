# week17-6.py
# LeetCode 2462. Total Cost to Hire K Workers
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        if candidates * 2 + k > N:
            heapify(costs)
            ans = 0
            for i in range(k): ans += heappop(costs)
            return ans
        heap1, heap2 = [], []
        for i in range(candidates):
            heappush(heap1, costs[i])
            heappush(heap2, costs[N-1-i])
        ans = 0
        left, right = candidates, N-candidates-1
        for i in range(k):
            if heap1[0] <= heap2[0]:
                ans += heappop(heap1)
                heappush(heap1, costs[left]); left += 1
            else:
                ans += heappop(heap2)
                heappush(heap2, costs[right]); right -= 1
        return ans
