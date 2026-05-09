class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=0
        i=0
        j=0
        while(j<len(t) and i<len(s)):
            print("i:",i)
            print("j:",j)
            if len(s)==0:
                return(True)
            else:    
                if s[i]==t[j]:
                    a+=1
                    i+=1
                    j+=1
                else:
                    j+=1
        if a==len(s):
            return(True)
        else:
            return(False)        
        