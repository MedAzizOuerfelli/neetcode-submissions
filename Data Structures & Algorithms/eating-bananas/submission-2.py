class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right :
            mid = (left + right) // 2
            count = 0
            for i in range(len(piles)):
                count += (mid + piles[i] - 1) // mid
            if count <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
