class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] *n
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2], dp[-1])
        for index in range(n - 3, -1, -1):
            roob = nums[index] + dp[index + 2]
            notRoob = dp[index + 1]
            dp[index] = max(roob, notRoob)
        return dp[0]