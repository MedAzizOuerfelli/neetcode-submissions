import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [nums[0]]
        res = 1
        for i in nums[1:]:
            if l[-1] < i:
                l.append(i)
                res += 1
                continue
            index = bisect.bisect_left(l, i)
            l[index] = i
        return res
            