# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        ch=head
        while ch is not None:
            nextt=ch.next
            c=ch
            c.next=prev
            prev=c
            ch=nextt
        return prev    
