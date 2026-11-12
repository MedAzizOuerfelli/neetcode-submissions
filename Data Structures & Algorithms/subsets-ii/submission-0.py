class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrakinf(index, cur):
            if index == len(nums):
                result.append(cur[:])
                return
            cur.append(nums[index])
            backtrakinf(index + 1, cur)
            cur.pop()

            nxt = index + 1
            while nxt < len(nums) and nums[index] == nums[nxt]:
                nxt += 1
            backtrakinf(nxt, cur)
        backtrakinf(0, [])
        return result