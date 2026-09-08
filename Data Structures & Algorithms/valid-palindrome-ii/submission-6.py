class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        main=s
        for i in range(len(s)):
            l=list(s)
            l.pop(i)
            if l==l[::-1]:
                return True
        return False        

        