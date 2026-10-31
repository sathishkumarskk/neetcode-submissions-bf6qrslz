class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==1:
            return s[::-1]
        a=s.split()
        a=[i[::-1] for i in a]  
        a=" ".join(a)
        return a  
