class Solution:
    def mySqrt(self, x: int) -> int:
        a=0
        i=0
        while(i*i<x):
            if (i*i)<x:
                a=i
            i+=1
        if (i*i)==x:
            return i
        else:
            return a        