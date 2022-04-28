#https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def ping(self, grid: List[List[int]], now):
        row, col = now[0], now[1]
        if grid[row][col]==1:
            if col+1 >= len(grid[0]) or grid[row][col+1]==-1:
                return -1
            elif grid[row][col+1]==1:
                if row == len(grid)-1:
                    return col+1
                else:
                    return self.ping(grid, (row+1, col+1))
        else:
            if col-1 < 0 or grid[row][col-1]==1:
                return -1
            elif grid[row][col-1]==-1:
                if row==len(grid)-1:
                    return col-1
                else:
                    return self.ping(grid, (row+1, col-1))
    
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        output = []
        for i in range(len(grid[0])):
            result = self.ping(grid, (0, i))
            output.append(result)
        return output                
        
        
