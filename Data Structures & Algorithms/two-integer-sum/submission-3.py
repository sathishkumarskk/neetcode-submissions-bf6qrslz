class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=nums
        t=target
        l=[]
        for i in range(0,len(n)):
            for j in range(0,len(n)):
                if len(l)!=2:
                 if i!=j:
                    if n[i]+n[j]==t:
                        l.extend([i,j])
                else:
                    break
        return(l)         
        