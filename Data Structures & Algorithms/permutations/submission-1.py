class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        result = []
        def backtraking(cur):
            if len(cur) == len(nums):
                result.append(cur[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                cur.append(nums[i])
                backtraking(cur)

                used[i] = False
                cur.pop()
        backtraking([])
        return result