class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        def backtraking(index, curSum, curArr):
            if curSum == target:
                result.append(curArr[:])
                return 
            if index >= len(nums) or curSum > target:
                return
            curArr.append(nums[index])
            backtraking(index + 1, curSum + nums[index], curArr)
            curArr.pop()
            nextIndex = index + 1
            while nextIndex < len(nums) and nums[nextIndex] == nums[index]:
                nextIndex += 1 
            
            backtraking(nextIndex, curSum, curArr)
        backtraking(0, 0, [])
        return result

