class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                result = max(result, prices[i] -buy)
        return result