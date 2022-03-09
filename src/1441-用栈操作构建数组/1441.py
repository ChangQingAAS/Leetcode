class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # 如果在，则直接push
        # 不在，则先push在pop

        res = []
        for item in range(1, n+1):
            if item > target[-1]:
                break
            
            if item in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        return res