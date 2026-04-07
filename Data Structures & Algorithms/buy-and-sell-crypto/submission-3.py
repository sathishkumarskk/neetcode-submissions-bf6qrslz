class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices
        li=[]
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if i!=j:
                    if i<j and l[i]<l[j]:
                        p=abs(l[i]-l[j])
                        li.append(p)
        if len(li)==0:
            return(0)
        else:    
            return(max(li))        