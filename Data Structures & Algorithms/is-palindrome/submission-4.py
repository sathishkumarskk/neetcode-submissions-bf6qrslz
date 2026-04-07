class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list(s)
        l=[i.lower() for i in l if i.isalnum()]
        print(l)
        print(l)
        left=0
        count=0
        right=len(l)-1
        while(left<right):
            if l[left]==l[right]:
                left+=1
                right+=-1
            else:
                count+=1
                return(False)
        return(True)        
        