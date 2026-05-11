class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        j=0
        while(i<len(nums)):
            if j==len(nums):
                i+=1
                j=0
            if i<len(nums):    
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    j+=1
                else:
                    j+=1    
        return(nums)            

           