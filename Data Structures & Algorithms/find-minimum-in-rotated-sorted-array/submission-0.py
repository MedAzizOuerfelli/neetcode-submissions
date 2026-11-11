class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = len(nums) - 1
        cur = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if cur > nums[left]:
                    cur = nums[left]
                left = mid + 1
            else:
                right = mid
        return cur