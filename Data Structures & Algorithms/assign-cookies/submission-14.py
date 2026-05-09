class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
     a=0
     i=0
     j=0
     g.sort()
     s.sort()
     print("g: ",g)
     print("s: ",s)
     while(i<len(g) and j<len(s)):
        print("i :",i)
        print("j:",j)
        if g[i]<=s[j]:
            print("--if--")
            i+=1
            j+=1
            a+=1
        else:
            print("--elif--")            
            j+=1

     return(a)           
