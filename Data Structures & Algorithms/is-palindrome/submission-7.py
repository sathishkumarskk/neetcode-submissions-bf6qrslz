class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list(s)
        l=[i.lower() for i in l if i!=" " and i.isalnum()]
        count=len(l)//2
        i=0
        j=len(l)-1
        m=0
        while(i<j):
            if l[i]==l[j]:
                i+=1
                j-=1
                m+=1
            else:
                break
        if m==count:
            return(True)
        else:
            return(False)     