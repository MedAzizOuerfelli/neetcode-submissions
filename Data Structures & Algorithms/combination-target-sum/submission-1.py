class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtraking(index, cur, curSum):
            if curSum == target:
                res.append(cur[:])
                return
            if index >= len(nums) or curSum > target:
                return 
            cur.append(nums[index])
            backtraking(index, cur, curSum + nums[index])
            cur.pop()
            backtraking(index + 1, cur, curSum)
        backtraking(0, [], 0)
        return res