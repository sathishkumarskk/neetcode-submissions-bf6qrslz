class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length=len(words)
        s="".join(words)
        l=list(s)
        m=list(set(l))
        for z in m:
            if l.count(z)%length!=0:
                return False
        return True         

        
        