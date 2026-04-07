class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while(i!=j):
            if nums.count(nums[i])>1:
                nums.pop(i)
                j=len(nums)-1
            else:
                i+=1
            if nums.count(nums[j])>1:
                nums.pop(j)
                j=len(nums)-1                
            else:
                j=len(nums)-1
        return(len(nums))               