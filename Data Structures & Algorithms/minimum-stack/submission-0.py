class node:
    def __init__(self,v):
        self.data=v
        self.next=None
class MinStack:

    def __init__(self):
        self.topp=None

    def push(self, val: int) -> None:
        n_node=node(val)
        n_node.next=self.topp
        self.topp=n_node

    def pop(self) -> None:
        if self.topp is None:
            return(None)
        self.topp=self.topp.next

    def top(self) -> int:
        if self.topp is None:
            return(None)        
        return(self.topp.data)

    def getMin(self) -> int:
        if self.topp is None:
            return(None)           
        mini=self.topp.data
        temp=self.topp
        while(temp!=None):
            if temp.data<mini:
                mini=temp.data
            temp=temp.next
        return(mini)        