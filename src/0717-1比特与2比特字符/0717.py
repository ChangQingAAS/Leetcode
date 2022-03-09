class Solution:
    def isOneBitCharacter(self,bits ) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                # 跳两步
                i += 2
                print(i)
            elif bits[i] == 0:
                # 跳一步
                i += 1
                print(i)

        return i == len(bits) - 1
