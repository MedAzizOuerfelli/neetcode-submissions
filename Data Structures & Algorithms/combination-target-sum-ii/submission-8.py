class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        def backtraking(start, curSum, curArr):
            if curSum == target:
                result.append(curArr[:])
                return 
            if curSum > target:
                return
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if  i - 1 >= 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                curArr.append(nums[i])
                used[i] = True
                backtraking(i + 1, curSum + nums[i], curArr)

                curArr.pop()
                used[i] = False
        backtraking(0, 0, [])
        return result

