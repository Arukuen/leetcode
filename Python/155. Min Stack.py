class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None or self.min > val:
            self.min = val

    def pop(self) -> None:
        if self.stack == []:
            return None
        self.stack.pop()
        if self.stack == []:
            self.min = None
        else:
            self.min = min(self.stack)

    def top(self) -> int:
        if self.stack == []:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min