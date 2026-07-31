class MinStack:

    def __init__(self):
        self.s=[]
        self.ms=[]
    def push(self, val: int) -> None:
        #chk if not full
        self.s.append(val)
        if not self.ms :
            self.ms.append(val)
        elif self.ms[-1]>val:
            self.ms.append(val)
        else:
            self.ms.append(self.ms[-1])
        

    
        

    def pop(self) -> None:
        
        self.s.pop()
        self.ms.pop()
        

    def top(self) -> int:
        if self.s :
            return self.s[-1]

    def getMin(self) -> int:
        if self.ms:
            return self.ms[-1]
        
