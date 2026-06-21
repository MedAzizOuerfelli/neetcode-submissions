class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        s2 = set(nums2)
        for num in nums1:
            if num in s2:
                result.append(num)
                s2.remove(num)
        return result