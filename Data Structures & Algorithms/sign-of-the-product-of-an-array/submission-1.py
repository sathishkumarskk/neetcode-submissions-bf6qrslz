class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            s*=nums[i]  
        if s>0:
            return 1
        elif s==0:
            return 0
        else:
            return -1            