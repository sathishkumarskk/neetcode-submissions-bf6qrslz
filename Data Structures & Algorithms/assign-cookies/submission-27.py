class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        c=0
        print(g)
        print(s)
        while(i<len(g) and j<len(s)):
            print(g[i],s[j])
            print()
            if s[j]>=g[i]:
                c+=1
                i+=1
                j+=1
            elif g[i]>s[j]:
                j+=1
            else:
                i+=1
        return(c)                

        