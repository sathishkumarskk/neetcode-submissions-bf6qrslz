class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            while i<len(nums) and nums[i]<0:
                i+=1
            while j<len(nums) and nums[j]>0 :
                j+=1

            a.append(nums[i])
            a.append(nums[j]) 
            i+=1
            j+=1 
        return(a)              
            
                


        