class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0

        m = 0
        n = len(people) - 1
        while m <= n:
            while m < n and people[m] + people[n] > limit:
                n -= 1
                ans += 1
            m += 1
            n -= 1
            ans += 1

        return ans
