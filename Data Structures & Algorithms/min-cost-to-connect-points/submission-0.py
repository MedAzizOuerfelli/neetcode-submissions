class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            x,y=points[i]
            for j in range(i+1,n):
                a,b=points[j]
                cost=abs(a-x)+abs(b-y)
                graph[(x,y)].append([cost, a, b])
                graph[(a,b)].append([cost, x, y])
        visited = set()
        minheap = [(0, points[0][0], points[0][1])]
        res = 0
        while minheap:
            cost, x, y = heapq.heappop(minheap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += cost
            if len(visited) == n:
                return res
            for w, neiX, neiY in graph[(x, y)]:

                heapq.heappush(minheap, (w, neiX, neiY))
