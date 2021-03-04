class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n, orig = len(grid), len(grid[0]), grid[r0][c0] # dimensions 
        seen = {(r0, c0)}
        stack = [(r0, c0)]
        
        def dfs(start):
            i,j = start
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if (ii, jj) not in seen:
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == orig: 
                        seen.add((ii, jj))
                        dfs((ii,jj))
                    else:
                        grid[i][j] = color 
        dfs((r0,c0))
        return grid 