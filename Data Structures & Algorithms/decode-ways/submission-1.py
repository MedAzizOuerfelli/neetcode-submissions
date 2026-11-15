class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in memo:
                return memo[index]
            take1 = dfs(index + 1)
            if index + 1 < len(s) and s[index: index + 2] <= "26":
                take2 = dfs(index + 2)
                memo[index] = take2 + take1
                return memo[index]
            else:
                memo[index] = take1
                return memo[index]
        return dfs(0)