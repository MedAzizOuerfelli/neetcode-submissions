class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        result = 0
        for key in d:
            if d[key] == 1:
                return -1
            result += math.ceil(d[key]/3)
        
        return result