class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=nums
        t=target
        found=0
        v=0
        for i in n:
            if i==t:
                found=n.index(i)
                return(found)
                break
            else:
                v+=1
        if v==len(n):
            return(-1)   