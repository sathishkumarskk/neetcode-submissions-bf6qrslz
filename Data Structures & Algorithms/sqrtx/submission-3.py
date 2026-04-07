class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        v=0
        while((i*i)<=x):
            v=i
            i+=1
        return(v)    
    