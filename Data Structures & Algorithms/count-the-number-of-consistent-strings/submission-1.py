class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            a=True
            for j in i:
                if j not in allowed:
                    a=False
            if a==True:
                c+=1        
        return c           
        