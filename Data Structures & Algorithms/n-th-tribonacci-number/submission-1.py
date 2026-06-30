class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1   
        elif n==2:
            return 1
        elif n==3:
            return 2         
        l=[0,1,1]       
        while(len(l)<=n):
            l.append(l[-1]+l[-2]+l[-3])
        print(l)    
        return l[n]    