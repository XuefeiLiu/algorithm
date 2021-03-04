from collections import deque

class Solution(object):
    def bfs(self,heights,k):
        m = len(heights)
        n = len(heights[0])
        q = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        while q:
            i,j = q.popleft()
            if i==m-1 and j == n-1:
                return True
            for x,y in [[-1,0],[0,-1],[0,1],[1,0]]:
                ni = i + x
                nj = j + y
                
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visited:
                    if abs(heights[ni][nj] - heights[i][j])<=k:
                        q.append((ni,nj))
                        visited.add((ni,nj))

                    
        return False
        
        
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        if not heights:
            return 0
        maxHeight = 0 
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                if heights[i][j] > maxHeight:
                    maxHeight = heights[i][j]
        start = 0
        end = maxHeight
        while start<end:
            mid = (start+end)//2
            if self.bfs(heights,mid):
                end = mid
            else:
                start = mid +1
        return start
            