class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in range(len(nums)):
            length = 1
            if nums[i] - 1 not in s:
                while nums[i] + length in s:
                    length += 1
                longest = max(longest, length)
        return longest