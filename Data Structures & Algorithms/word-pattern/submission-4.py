class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        p=list(pattern)
        if len(set(s))!=len(set(p)) or len(pattern)!=len(s):
            return False
        return True      
        