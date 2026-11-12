class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtraking(index,curSum):
            if curSum == target:
                res.append(cur[:])
                return
            if index >= len(nums) or curSum > target:
                return 
            cur.append(nums[index])
            backtraking(index, curSum + nums[index])
            cur.pop()
            backtraking(index + 1, curSum)
        backtraking(0,0)
        return res