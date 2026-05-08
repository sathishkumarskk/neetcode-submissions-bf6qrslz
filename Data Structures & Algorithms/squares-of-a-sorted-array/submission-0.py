class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        j=len(nums)-1
        while(i<=j):
            if i==j:
               a.append(nums[i]*nums[i])
            else:  
               a.append(nums[j]*nums[j])
               a.append(nums[i]*nums[i])    
            i+=1
            j-=1
        a.sort()    
        return(a)    

        