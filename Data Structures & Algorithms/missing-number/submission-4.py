class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        found=0
        for i in nums:
            if i==0:
                found=1
        if found==1:        
                n=nums
                n.sort()
                l=len(n)-1
                for i in range(0,len(n)):
                    if i<l:
                     if n[i]+1!=n[i+1]:
                        return(n[i]+1)
                        break
                    else:
                         return(n[l]+1)
                         break
        else:
            n=nums
            n.sort()
            l=len(n)-1
            for i in range(0,len(n)):
                if i<l:
                 if n[i]+1!=n[i+1]:
                    return(n[i]+1)
                    break
                else:
                     return(0)
                     break           
        