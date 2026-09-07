class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a=[]
        i=0
        m=1        
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                m+=1
            else:
                a.append(m)
                m=1
            i+=1 
        a.append(m)      
        m=1  
        i=0   
        while i<len(nums)-1:
            print("value:",nums[i],nums[i+1])
            if nums[i]>nums[i+1]:
                m+=1
            else:
                a.append(m)
                m=1
            i+=1    
        a.append(m)    
        return max(a)                        
