"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""




class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        self.height = len(grid)
        self.length = len(grid[0])
        for i in range(self.height):
            for j in range(self.length):
                if grid[i][j] == 1:
                    max_area = max(max_area,self.dfs(grid,i,j))
        return max_area
    
    def dfs(self,grid,i,j):
        if(i < 0 or i >= self.height or j < 0 or j >=self.length or grid[i][j]==0):
            return 0
        grid[i][j] = 0
        area = 1
        area+=self.dfs(grid,i,j+1)
        area+=self.dfs(grid,i,j-1)
        area+=self.dfs(grid,i-1,j)
        area+=self.dfs(grid,i+1,j)
        return area
