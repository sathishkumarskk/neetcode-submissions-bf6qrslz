class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=s
        s=n.lower()
        straight="".join([i for i in s if i.isalnum()])
        reverse=straight[::-1]
        if straight==reverse:
            return True
        else:
            return False        