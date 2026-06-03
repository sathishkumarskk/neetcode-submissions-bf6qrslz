class MyQueue:

    def __init__(self):
        self.q1=[]
        self.q2=[]        

    def push(self, x: int) -> None:
               self.q1.append(x)
               self.q1.extend(self.q2)    
               self.q2[:]=self.q1
               self.q1.clear()        

    def pop(self) -> int:
        return(self.q2.pop())
        

    def peek(self) -> int:
        return(self.q2[-1])
        

    def empty(self) -> bool:
        if len(self.q2)==0:
            return(True)
        else:
            return(False)    
        
