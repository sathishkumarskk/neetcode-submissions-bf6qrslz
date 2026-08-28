# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s=0
        c=0
        current=head
        reverse=None
        while current is not None:
            c+=1
            n=ListNode(current.val)
            n.next=reverse
            reverse=n
            current=current.next
        count=0  
        t1=head
        t2=reverse         
    
        while count<=(c/2):
            if (t1.val+t2.val)>s:
                s=t1.val+t2.val
            count+=1
            t1=t1.next
            t2=t2.next 
        return s        


        