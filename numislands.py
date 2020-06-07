"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""



class Solution:
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        numIslands = 0
        self.height = len(grid)
        self.length = len(grid[0])
        for i in range(self.height):
            for j in range(self.length):
                if grid[i][j] == "1":
                    numIslands+=self.dfs(grid,i,j)
        return numIslands
    
    def dfs(self,grid,i,j):
        if(i < 0 or i >= self.height or j < 0 or j >=self.length or grid[i][j]=="0"):
           return 0 
        grid[i][j] = "0"
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        return 1

if __name__ == '__main__':
    sol = Solution()
    ex1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert sol.numIslands(ex1) == 1
    ex2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    assert sol.numIslands(ex2) == 3
