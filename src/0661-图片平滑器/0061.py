class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])
        res = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                count = 0
                for nr in (r - 1, r , r+1):
                    for nc in (c - 1,c, c+1):
                        if 0 <= nr < rows and 0 <= nc < columns:
                            res[r][c] += img[nr][nc]
                            count += 1
                res[r][c] //= count
        return res