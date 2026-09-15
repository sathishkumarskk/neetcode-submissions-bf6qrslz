class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in nums:
            if nums.count(i)>c:
                c=nums.count(i)
                d=i
        i=0
        while i<len(nums):        
            if nums[:i+1].count(d)>len(nums[:i+1])/2 and nums[i+1:].count(d)>len(nums[i+1:])/2:
                    return i
            i+=1  
        return -1                

        