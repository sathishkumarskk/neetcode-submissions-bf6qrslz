# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        temp=head
        while temp is not None:
            a.append(str(temp.val))
            temp=temp.next
        b="".join(a) 
        if b==b[::-1]:
            return True
        return False               