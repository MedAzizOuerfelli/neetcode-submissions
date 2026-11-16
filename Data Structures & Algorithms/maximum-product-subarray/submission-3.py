class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        res = max(nums)
        nums = [-3,0,-2]
                i

        prefix = -3 * 0      
        suffix = -2 * 0
        
        """
        n = len(nums)
        res = nums[0]
        prefix = suffix = 0
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n -1 -i]
            res = max(res, max(prefix, suffix))
        return res