class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_dict = {}
        stack = []
        for item in nums2:
            if not stack:
                stack.append(item)
            else:
                while stack:
                    top = stack[-1]
                    if item > top:
                        map_dict[top] = item
                        stack.pop()
                    else:
                        stack.append(item)
                        break
                stack.append(item)
        for item in stack:
            map_dict[item] = -1

        res = []
        for item in nums1:
            res.append(map_dict[item])
        return res