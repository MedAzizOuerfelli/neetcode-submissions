class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for index in range(n - 1, -1, -1):
            take1 = dp[index + 1] if s[index] != "0" else 0
            if index + 1 < len(s) and "10"<=s[index: index + 2] <= "26":
                take2 = dp[index + 2]
                dp[index] = take2 + take1
                
            else:
                dp[index] = take1
        return dp[0]
    