class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        s = set()
        minheap = [(0, k)]
        res = 0
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in s:
                continue
            s.add(node)
            res = cost
            if len(s) == n:
                return res
            for nei, neiCost in graph[node]:
                heapq.heappush(minheap, (neiCost + cost, nei))
        return -1
            
