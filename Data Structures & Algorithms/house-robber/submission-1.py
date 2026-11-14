class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            roob = nums[index] + dfs(index + 2)
            notRoob = dfs(index + 1)
            memo[index] = max(roob, notRoob)
            return memo[index]
        return dfs(0)