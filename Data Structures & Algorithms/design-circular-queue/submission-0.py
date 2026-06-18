class MyCircularQueue:
    def __init__(self, k: int):
        self.l=[]
        self.k=k
    def enQueue(self, value: int) -> bool:
        if len(self.l)==self.k:
            return False
        self.l.append(value)
        return True

    def deQueue(self) -> bool:
        if self.l==[]:
            return False
        self.l.pop(0)
        return True

    def Front(self) -> int:
        if self.l==[]:
            return -1
        return self.l[0]

    def Rear(self) -> int:
        if self.l==[]:
            return -1
        return self.l[-1]

    def isEmpty(self) -> bool:
        s=0
        for i in self.l:
            s+=i
        if s==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.l)==self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()