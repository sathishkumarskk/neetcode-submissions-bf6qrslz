class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1
        while(j<len(nums) and i<len(nums)):
          if i>=j:
            j+=1
          else:  
            if nums[i]==0:
              if nums[j]==0:
                j+=1
              else:
                nums[i],nums[j]=nums[j],nums[i]   
                i+=1
            else:
              i+=1    
          