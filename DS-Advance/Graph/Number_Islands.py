"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        visit = set()
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(row,column):
            queue = collections.deque()
            visit.add((row,column))
            queue.append((row,column))
            while queue:
                row,col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    newrow = row + dr if row + dr < rows else rows-1
                    newcol = col + dc if col + dc < cols else cols-1
                    if grid[newrow][newcol] == "1" and newrow in range(rows) and newcol in range(cols) and (newrow,newcol) not in visit :
                        queue.append((newrow,newcol))
                        visit.add((newrow,newcol))
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    numIslands += 1
        return numIslands
    
if __name__ == "__main__":
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    print(Solution().numIslands(grid))