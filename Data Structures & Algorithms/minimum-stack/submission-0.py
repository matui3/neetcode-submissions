class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minVal = self.stack[-1]
        while self.stack:
            current = self.stack.pop()
            minVal = min(minVal, current)
            self.minStack.append(current)
        
        while self.minStack:
            self.stack.append(self.minStack.pop())

        return minVal