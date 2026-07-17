class MinStack:

    def __init__(self):
        self.l=[]
     
    def push(self, value: int) -> None:
        self.l.append(value)
        

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return min(self.l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()