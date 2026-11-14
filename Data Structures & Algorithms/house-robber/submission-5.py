class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        one = 0
        two = 0
        for index in range(n):
            temp = max(one, nums[index] + two)
            two = one
            one = temp

        return one