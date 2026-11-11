class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right :
            mid = (left + right) // 2
            count = 0
            for i in range(len(piles)):
                if mid >= piles[i] :
                    count += 1
                else:
                    count += piles[i] // mid
                    if (piles[i] % mid) != 0:
                        count += 1 
            if count <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
