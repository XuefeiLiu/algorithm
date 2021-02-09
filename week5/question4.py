class Solution(object):
    def __init__(self):
        self.count = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        def dfs(grid,i,j):
            if i<0 or i>m-1:
                return
            if j< 0 or j>n-1:
                return
            if grid[i][j] =='0':
                return
            grid[i][j] = '0'
            for pi,pj in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(grid,i+pi,j+pj)

    
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1':
                    self.count+=1
                    dfs(grid,i,j)
                    
                    
        return self.count