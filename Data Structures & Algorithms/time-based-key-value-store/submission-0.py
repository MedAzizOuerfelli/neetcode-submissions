class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.keyStore[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if self.keyStore[key][mid][1] <= timestamp:
                res = self.keyStore[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
