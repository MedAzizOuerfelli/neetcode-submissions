class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backTraking(index, cur):
            if index == len(nums):
                result.append(cur[:])
                return 
            
            cur.append(nums[index])
            backTraking(index + 1, cur)
            cur.pop()
            backTraking(index + 1, cur)
        backTraking(0, [])
        return result