"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        heap = []
        for i in intervals:
            start, end  = i.start, i.end
            if heap and heap[0][0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, (end, start))
        return len(heap)