class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=set(ransomNote)
        m=set(magazine)
        for i in r:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True        
        