class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i] not in a:
                print("--if--")
                a.append(s[i])
                if t[i] not in b:
                  b.append(t[i])
                else:
                    return False  
            else:
                print("s[i]:",s[i])
                indexx=a.index(s[i])
                print("index:",indexx)
                print("list of a:",a)                
                print("list of b:",b)
                if b[indexx]!=t[i]:
                    return False
        return True                
        