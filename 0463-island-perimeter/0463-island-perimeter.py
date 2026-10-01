class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        length=len(grid[0])
        breadth=len(grid)
        perimeter=0
        for i in range(breadth):
            for j in range(length):
                if grid[i][j]==1:
                        if i>0:
                            up=grid[i-1][j]
                            if up==0:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if i+1<breadth:
                            down=grid[i+1][j]
                            if down==0:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if j>0:
                            left=grid[i][j-1]
                            if left==0:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if j+1<length:
                            right=grid[i][j+1]
                            if right==0:
                                perimeter+=1
                        else:
                            perimeter+=1
        return perimeter
        