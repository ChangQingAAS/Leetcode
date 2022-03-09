class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            sum = 0
            while n > 0:
                sum += (n%10)**2
                n = n //  10
            return sum


        hash_table = dict()
        while n not in hash_table:
            if n == 1:
                return True
            hash_table[n] = None
            n = get_next(n)
        return False

# 考虑一些特殊情况，比如无限循环，数值无限增大
#### 为什么不会无限变大

# * 如果是一位数，最大为9，平方和最大是81
# * 如果是两位数，最大为99，平方和最大为162
# * 如果是三位数，最大为999，平方和最大为243
# * 如果是四位数，最大为9999，平方和最大为324

# **所以对于三位数的整数，它的下一个数字（每个位置数字的平方和）不会大于243，对于四位和四位以上的整数，每次计算都会减小，最终变为三位数的整数，所以结果不会无限增大，算法可能会在243以下的所有数字上循环，然后回到它已经到过的一个循环或者回到1。**
# 对于循环的情况，可以把每次算到的结果放进hash表内，如果进入 while前，发现其在hash表内，则该数字是一个循环，直接退出