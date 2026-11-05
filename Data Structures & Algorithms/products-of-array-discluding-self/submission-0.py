class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = [nums[0]]
        right = [nums[-1]]
        for num in nums[1:]:
            left.append(left[-1] * num)
        for i in range(len(nums) - 2, -1, -1):
            right.append(right[-1] * nums[i])
        right.reverse()
        for i in range(len(nums)):
            if i - 1 >= 0 and i + 1 < len(nums):
                res.append(right[i+1]*left[i-1])
            elif i - 1 >= 0:
                res.append(left[i-1])
            else:
                res.append(right[i+1])
        return res
