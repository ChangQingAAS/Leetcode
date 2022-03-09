# 根本思路：基本都是n个计数 （取min) => 1个计数，再按出现次数进行输出
# 可能计数方法会有一些不同例如cnt[str - 'a' ],或者直接cnt['a']

import collections
from functools  import reduce

class Solution:
    def commonChars(A):
        # map 用来给每个A的元素中的字符次数
        # reduce 调用__and__ 返回的是这几个A[i]中各元素的最小值
        result = reduce(collections.Counter.__and__, map(collections.Counter, A))
        # print(result) # => Counter({'l': 2, 'e': 1})
        # print(result.elements()) # => <itertools.chain object at 0x000001E358403100>
        # for x in result.elements():
        #     print(x,end=" ") # => e l l
        return list(result.elements())