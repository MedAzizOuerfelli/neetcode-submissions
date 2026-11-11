class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left < right :
            mid = (left + right) // 2
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)
            if count <= h:
                res = mid
                right = mid
            else:
                left = mid + 1
        return left
