class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=list(set(nums))
        l.sort()
        p=[i for i in l if i>0]
        if len(p)==0:
            return(1)
        elif min(p)!=1:
            return(1)  
        else: 
            for i,j in zip(range(min(p),max(p)),p):
               if i!=j:
                 return(i)
        return(max(p)+1)        
        