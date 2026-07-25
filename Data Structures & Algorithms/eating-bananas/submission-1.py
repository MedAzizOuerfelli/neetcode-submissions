class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

