class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # 法一
        #if A == sorted(A) or A == sorted(A, reverse = True):
        #    return True
        #return False
        #法2
        return all([A[i] <= A[i+1] for i in range(len(A)-1)]) or all([A[i] >= A[i+1] for i in range(len(A) - 1)])