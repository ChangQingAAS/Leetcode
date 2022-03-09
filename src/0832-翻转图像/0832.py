class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            # 水平翻转
            row.reverse()
            #0 1 替换
            new_row = [0 if item else 1 for item in row]

            res.append(new_row)
        return res
            