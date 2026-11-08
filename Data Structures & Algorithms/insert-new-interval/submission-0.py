class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            start, end  = intervals[i][0], intervals[i][1]
            if start > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0]  > end :
                result.append([start, end])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        result.append(newInterval)
        return result


