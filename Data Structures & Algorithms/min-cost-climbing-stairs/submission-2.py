class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == len(cost):
                return 0
            if i > len(cost):
                return float("inf")
            if i in memo:
                return memo[i]
            one = dfs(i + 1) + cost[i] 
            two = dfs(i + 2) + cost[i] 
            memo[i] = min(one, two)
            return memo[i]
        return min(dfs(0), dfs(1))
