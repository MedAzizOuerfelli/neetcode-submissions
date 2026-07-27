class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans1 = []
        s = set()
        for num in nums1:
            if num not in s2 and num  not in s:
                s.add(num)
                ans1.append(num)
        s = set()
        ans2 = []
        for num in nums2:
            if num not in s1 and num not in s:
                s.add(num)
                ans2.append(num)
        return [ans1, ans2]