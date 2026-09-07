class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a=[]
        for i,j in zip(nums,range(0,len(nums))):
            if i!=j:
                return j
        if len(a)==0:
            return j+1        
        return -1        
        