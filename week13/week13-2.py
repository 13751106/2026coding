# week13-2.py
# LeetCode 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==2:
                    visited.add( (i,j) )
                    queue.append( (i,j,0) )
                if grid[i][j]==1: fresh += 1
        if fresh==0: return 0
        ans = -1
        while queue:
            i,j,t = queue.popleft()
            ans = t
            for ii, jj in (i+1, j),(i-1, j), (i, j+1),(i, j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue
                if (ii,jj) in visited: continue
                if grid[ii][jj]==1:
                    fresh -= 1
                    visited.add( (ii,jj) )
                    queue.append( (ii,jj,t+1) )
        if fresh>0: return -1
        return ans
