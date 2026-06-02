class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
               self.q2.append(x)
               self.q2.extend(self.q1)    
               self.q1[:]=self.q2
               self.q2.clear()

    def pop(self) -> int:
        return(self.q1.pop(0))
        

    def top(self) -> int:
        return(self.q1[0])
        

    def empty(self) -> bool:
        if len(self.q1)==0:
            return(True)
        else:
            return(False)    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()