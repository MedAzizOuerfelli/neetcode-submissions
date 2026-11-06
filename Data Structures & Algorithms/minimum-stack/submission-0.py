class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minArr:
            self.minArr.append(val)
        
        else:
            self.minArr.append(min(self.minArr[-1], val))

    def pop(self) -> None:
        self.minArr.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
