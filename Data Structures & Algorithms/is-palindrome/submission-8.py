class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list(s)
        l=[i.lower() for i in l if i!=" " and i.isalnum()]
        count=len(l)//2
        i=0
        j=len(l)-1
        m=0
        while(i<j):
            if l[i]!=l[j]:
                return False
            else:
                i+=1
                j-=1    
        return True            