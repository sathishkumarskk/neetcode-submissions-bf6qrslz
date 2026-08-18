# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c=0
        temp=head
        a=[]
        while temp is not None:
            if temp not in a:
              a.append(temp)
            else:
                return True  
            temp=temp.next
        return False 

        