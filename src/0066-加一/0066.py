class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #法1：类型转换
        num = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in str(num)]
        #法2:直接进行数学运算，只有+1=10的情况下才会进位
        """
        从个位数开始+1，如果等于10，就取余向前进一位
        如果不等于10直接返回
        """
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
            
        digits.insert(0,1)

        return digits