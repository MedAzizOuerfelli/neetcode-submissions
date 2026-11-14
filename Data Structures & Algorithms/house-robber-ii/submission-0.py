class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index, flag):
            if index >= len(nums) or (flag and index == len(nums) - 1):
                return 0
            key = (index, flag)
            if key in memo:
                return memo[key]
            if index == 0:
                take = nums[index] + dfs(index + 2, True)
            else:
                take = nums[index] + dfs(index + 2, flag)
            memo[key] = max(dfs(index + 1, flag), take)
            return memo[key]
        return dfs(0, False)