class Solution:
    def largeGroupPositions(self, nums: str) -> List[List[int]]: 
        """
        分析：
            遍历数组
            current_s 记录当前计数的字母
            current_s_count 记录当前计数字母的数量
            注意遍历结束后 current_s_count >=3的情况
        """
        result = []
        current_s = None
        current_s_count = 0
        for index, s in enumerate(nums):
            if not current_s:
                current_s = s
                current_s_count += 1
            else:
                if s == current_s:
                    current_s_count += 1
                else:
                    if current_s_count >= 3:
                        result.append([index-current_s_count,index -1])
                    current_s = s
                    current_s_count = 1
        
        # 还有一个
        if current_s_count >= 3:
            result.append([len(nums) - current_s_count, len(nums) -1])

        return result