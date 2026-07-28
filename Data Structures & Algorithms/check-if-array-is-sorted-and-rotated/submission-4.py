class Solution:
    def check(self, nums: List[int]) -> bool:
        i=nums.index(min(nums))
        c=0
        while c<len(nums)-1:
            print("value:",nums[i])
            if i==len(nums)-1:
                if nums[i]>nums[0]:
                    return False
                i=0    
            else:  
                if nums[i]>nums[i+1]:
                    return False   
                i+=1    
            c+=1    
            print()    
        return True                            

            
        