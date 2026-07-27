class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(curSum):
            if curSum > amount :
                return float("inf")
            if curSum == amount :
                return 0
            if curSum in memo:
                return memo[curSum]
            result = float("inf")
            for coin in coins:
                result = min(result, 1 + dfs(coin + curSum))
            memo[curSum] = result
            return result
        answer = dfs(0)
        return answer if answer != float("inf") else -1
