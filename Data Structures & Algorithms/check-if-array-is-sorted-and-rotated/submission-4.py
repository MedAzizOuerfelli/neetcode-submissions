class Solution:
    def check(self, nums: List[int]) -> bool:
        mini = min(nums)
        index = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == mini:
                index = i
                break
        s = sorted(nums)
        x = index
        for i in range(n):
            if s[i] != nums[(i+x)%n]:
                return False
        return True