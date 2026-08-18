# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=head
        while temp is not None:
            c+=1
            temp=temp.next
        print("c:",c)    
        c=c//2
        print("after:",c)
        t=head
        count=0
        while t is not None:
            if count<c:
                head=head.next   
            t=t.next 
            count+=1
        return head    
                          
        