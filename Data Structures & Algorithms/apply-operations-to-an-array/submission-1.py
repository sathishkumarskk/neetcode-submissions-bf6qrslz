class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        while j<len(nums):
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
            i+=1
            j+=1
        return [i for i in nums if i!=0]+ [i for i in nums if i==0]    

