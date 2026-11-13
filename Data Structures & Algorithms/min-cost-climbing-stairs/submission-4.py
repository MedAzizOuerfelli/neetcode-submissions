
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 2)

        dp[n] = 0

        for i in range(n - 1, -1, -1):
            one = dp[i + 1] + cost[i]
            two = dp[i + 2] + cost[i]
            dp[i] = min(one, two)

        return min(dp[0], dp[1])
