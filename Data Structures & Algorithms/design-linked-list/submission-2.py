class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.top=None

    def get(self, index: int) -> int:
        i=0
        temp=self.top
        while temp is not None:
            if i==index:
                return temp.data
            i+=1
            temp=temp.next
        return -1    

    def addAtHead(self, val: int) -> None:
    
           n=node(val)
           n.next=self.top
           self.top=n

    def addAtTail(self, val: int) -> None:
        if self.top is None:
             self.top=node(val)
             return self.top
        t=self.top
        while t.next is not None:
            t=t.next  
        t.next=node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        t=self.top
        while t is not None:
            if index==0:
                n=node(val)
                n.next=self.top
                self.top=n
                return
            if i==index-1:
                n=node(val)
                n.next=t.next
                t.next=n 
                return
            t=t.next   
            i+=1          
        


    def deleteAtIndex(self, index: int) -> None:
        ind=1
        t=self.top
        t1=self.top.next
        while t1 is not None:
            if ind==index:
                t.next=t.next.next
            ind+=1
            t=t.next
            t1=t1.next            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)