class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while(len(nums)!=len(set(nums))):
             if nums.count(nums[i])>1:
                nums.pop(i)
                j=len(nums)-1 
             else:
                i+=1
                j=len(nums)-1 
             print(nums)     
             print(i)
             print(j)   
             if nums.count(nums[j])>1:
                nums.pop(j)
             else:
                j-=1    
        return(len(nums))                      
