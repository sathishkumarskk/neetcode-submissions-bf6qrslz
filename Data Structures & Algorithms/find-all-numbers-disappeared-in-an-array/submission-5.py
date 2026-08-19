class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=list(set(nums))
        z=[]
        b=[i for i in range(1,len(nums)+1)]
        for j in b:
            if j not in a:
                z.append(j)     
        return z        
        