class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def fct(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if x in memo:
                return memo[x]
            one = fct(x + 1)
            two = fct(x + 2)
            memo[x] = one + two
            return memo[x]
        return fct(0)