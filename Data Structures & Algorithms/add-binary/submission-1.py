class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a,2)
        d=int(b,2)
        r=c+d
        z=bin(r)[2:]
        return z
        