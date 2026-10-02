class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        columns=len(grid[0])
        rows=len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter = 0
        for i in range(rows):
                    for j in range(columns):

                        if grid[i][j] == 1:

                            for di, dj in directions:
                                ni = i + di
                                nj = j + dj

                                # Outside the grid = water
                                if ni < 0 or ni >= rows or nj < 0 or nj >= columns:
                                    perimeter += 1

                                # Neighbor is water
                                elif grid[ni][nj] == 0:
                                    perimeter += 1
        return perimeter
        