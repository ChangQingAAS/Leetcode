# 网格的总和是 45，因为网格必须是 1 到 9 不同的数字。
# 每一列和行加起来必须是 15，乘以 3 则是网格的总和。
# 对角线的和也必须是 15，题目中说了对角线与列，行的和相同。
# 将四条穿过中心的线的 12 个值相加（即一行一列两条对角线），
# 这四条线加起来等于 60；而整个网格加起来为 45。
# 则中心等于 （60-45）/3 = 5
def numMagicSquaresInside(grid):
    rows = len(grid)
    columns = len(grid[0])
    if rows < 3 or columns < 3:
        return 0

    def magic(a, b, c, d, e, f, g, h, i):
        if (sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10))
                and
                (a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g == 15)):
            return True

    count = 0
    for r in range(0, rows-2):
        for c in range(0, columns-2):
            if grid[r+1][c+1] != 5:
                # 中心元素必须是5
                continue
            if magic(grid[r][c], grid[r][c + 1], grid[r][c + 2],
                     grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                     grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]):
                count += 1
    return count