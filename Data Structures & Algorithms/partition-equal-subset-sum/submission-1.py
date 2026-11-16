class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        memo = {}
        def dfs(index, cur_sum):
            if target == cur_sum:
                return True
            if index >= len(nums):
                return False
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]
            take = dfs(index + 1, cur_sum + nums[index])
            notTake = dfs(index + 1, cur_sum)
            memo[(index, cur_sum)] = take or notTake
            return memo[(index, cur_sum)]
        return dfs(0, 0)
