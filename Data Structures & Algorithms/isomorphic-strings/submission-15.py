class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i] not in a:
                a.append(s[i])
                if t[i] not in b:
                  b.append(t[i])
                else:
                    return False  
            else:
                indexx=a.index(s[i])
                if b[indexx]!=t[i]:
                    return False
        return True                
        