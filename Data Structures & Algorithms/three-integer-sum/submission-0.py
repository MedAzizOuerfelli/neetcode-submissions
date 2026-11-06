class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for k in range(len(nums)):
            if nums[k] > 0:
                return result
            if k - 1 >= 0 and nums[k] == nums[k- 1]:
                continue
            left, right = k + 1, len(nums) - 1
            while left < right:
                ThreeSum = nums[k] + nums[left] + nums[right]
                if ThreeSum > 0:
                    right -= 1
                elif ThreeSum < 0:
                    left += 1
                else:
                    result.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result