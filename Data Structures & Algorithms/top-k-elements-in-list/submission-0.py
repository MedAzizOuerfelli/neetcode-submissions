class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)
        for num in freq:
            heap.append((-freq[num], num))
        heapq.heapify(heap)
        result = []
        while k > 0:
            fq, n = heapq.heappop(heap)
            result.append(n)
            k -= 1
        result.reverse()
        return result