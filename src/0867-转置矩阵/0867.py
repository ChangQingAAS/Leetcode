class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []

        row_num = len(A)
        col_num = len(A[0])

        # 创建一个空的转置矩阵
        res = [[0 for __ in range(row_num)] for _ in range(col_num)]

        for r in range(row_num):
            for c in range(col_num):
                res[c][r] = A[r][c]
            
        return res