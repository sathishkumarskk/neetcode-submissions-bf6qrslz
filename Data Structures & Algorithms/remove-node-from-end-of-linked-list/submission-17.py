class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=head
        temp=head.next
        count=head
        c=0
        while count is not None:
            c+=1
            count=count.next
        if n==1 and c==1:
            return None  
        if c==n:
            head=head.next             
        c=c-n
        loop_count=1  
        while temp is not None:
            print("while")
            if loop_count==c:
                print("loop count:",loop_count,":",c)
                prev.next=prev.next.next
                break
            loop_count+=1    
            prev=prev.next
            temp=temp.next
        return head    



        