class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[]
        for i in range(len(s)-1):
            a.append(abs(ord(s[i])-ord(s[i+1])))
        return sum(a)    
        