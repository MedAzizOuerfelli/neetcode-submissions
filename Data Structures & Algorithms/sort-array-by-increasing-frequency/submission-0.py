class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        x = sorted(d.items(), key=lambda x: (x[1], -x[0]))
        return [key for key, freq in x for _ in range(freq)]