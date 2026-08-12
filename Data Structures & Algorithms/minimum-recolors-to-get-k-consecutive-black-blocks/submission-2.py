class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=list(blocks)
        a=[]
        i=0
        j=k
        if len(blocks)==k:
            return l.count("W")
        while(j<len(blocks)):
            a.append(l[i:j].count("W"))
            i+=1
            j+=1
        return min(a)    



        