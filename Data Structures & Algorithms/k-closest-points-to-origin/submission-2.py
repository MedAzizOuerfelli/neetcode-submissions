class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [((x ** 2) + (y ** 2), [x, y]) for x, y in points] 
        heapq.heapify(heap)
        res = []
        while k > 0:
            dist, pt = heapq.heappop(heap)
            x, y = pt[0], pt[1]
            res.append([x, y])
            k -= 1
        return res