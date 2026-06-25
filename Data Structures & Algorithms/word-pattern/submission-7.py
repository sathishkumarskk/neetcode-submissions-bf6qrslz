class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(set(s))!=len(set(list(pattern))) or len(pattern)!=len(s):
            return False
        return True      
        