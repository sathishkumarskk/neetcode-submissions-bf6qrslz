class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        num=1
        while 4**num<=n:
            if 4**num==n:
                return True
            num+=1    
        return False         
