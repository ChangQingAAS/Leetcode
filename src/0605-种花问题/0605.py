class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1 and flowerbed[0] == 0:
            count = 1
        else:
            count = 0
            for i in range(0, length):
                if i == 0:
                    if flowerbed[0] == 0 and flowerbed[1] == 0:
                        flowerbed[i] = 1
                elif i == length - 1:
                    # 最右边
                    if flowerbed[length - 1] == 0 and flowerbed[length - 2] == 0:
                        count += 1
                        flowerbed[length - 1] = 1
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        count += 1
                        flowerbed[i] = 1

        if count >= n:
            return True
        return False