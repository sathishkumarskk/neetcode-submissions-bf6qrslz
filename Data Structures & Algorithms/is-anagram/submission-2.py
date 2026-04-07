class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(i for i in s if i.isalpha())
        l2=list(i for i in t if i.isalpha())
        l1.sort()
        l2.sort()
        if l1==l2:
            return True
        else:
            return False         