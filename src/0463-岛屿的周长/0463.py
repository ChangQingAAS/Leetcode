class Solution:
    def islandPerimeter(self, grid) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    # 用之前的来做判断
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter
