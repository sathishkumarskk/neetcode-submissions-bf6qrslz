class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        a=0
        if len(set(nums))==1:
            return(nums[0])
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if len(nums[i:j+1])>0 and sum(nums[i:j+1])>a:
                    if len(nums[i:j+1])==1:
                        a=sum(nums[i:j+1])
                    else:    
                        b=nums[i:j+1]
                        length=len(b)
                        count=1
                        for k in range(len(b)-1):
                            if b[k]<b[k+1]:
                                count+=1
                                if count==length:                       
                                  a=sum(nums[i:j+1])
        return a                
                    