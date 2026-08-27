# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        t1=list1
        t2=list2
        top=None
        if t1.val<t2.val:
            next=t1.next
            n=t1
            n.next=top
            top=n
            t1=next
        else:
            next=t2.next
            n=t2
            n.next=top
            top=n 
            t2=next                 
        while t1 is not  None and t2 is not None:
            if t1.val<t2.val:
                nextt=t1.next
                n=t1
                n.next=top
                top=n
                t1=nextt
            else: 
                nextt=t2.next
                n=t2
                n.next=top
                top=n
                t2=nextt
        while t1 is None and t2 is not None:
            nextt=t2.next
            n=t2
            n.next=top
            top=n
            t2=nextt
        while t1 is not None and t2 is None:
            nextt=t1.next
            n=t1
            n.next=top
            top=n      
            t1=nextt
        #reverse
        main=None
        temp=top
        while temp is not None:
            nextt=temp.next
            n=temp
            n.next=main
            main=n 
            temp=nextt          
        return main