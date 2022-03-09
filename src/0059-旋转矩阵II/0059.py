class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0,1),(1,0),(0,-1), (-1,0)]

        # init
        matrix = [[0] * n for _ in range(n)]
        row,col,dirs_index = 0,0,0
        for i in range(1, n*n +1):
            matrix[row][col] = i

            # 计算下一个填充位置
            dx,dy = dirs[dirs_index]
            r = row + dx
            c = col + dy
            # 改变方向
            if r >= n or r < 0 or c>= n or c<0 or matrix[r][c] > 0:
                dirs_index = (dirs_index + 1) % 4
                dx,dy = dirs[dirs_index]

            row = row + dx
            col = col +dy
        return matrix
                
# **模拟四个方向**

# * 从左向右：行索引不变，列索引增大
# * 从上向下：行索引增大，列索引不变
# * 从右向左：行索引不变，列索引减小
# * 从下向上：行索引减小，列索引不变
# * 初始化元素全部为0，当索引越界，或者碰到不为0的值，就应该改变方向