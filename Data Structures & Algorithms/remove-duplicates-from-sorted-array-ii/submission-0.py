class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if result < 2 or num != nums[result - 2]:
                nums[result] = num
                result += 1
        return result