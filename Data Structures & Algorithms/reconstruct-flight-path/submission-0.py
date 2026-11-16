class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for from_i, to_i in sorted(tickets)[::-1]:
            graph[from_i].append(to_i)

        stack = ["JFK"]
        res = []
        while stack:
            node = stack[-1]
            if not graph[node]:
                res.append(stack.pop())
            else:
                stack.append(graph[node].pop())
        return res[::-1]
        

