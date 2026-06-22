class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        a=[]
        for i in nums:
           if nums.count(i)>1:
            a.append(i)
            break
        d=sorted(set(nums))    
        for i,j in zip(nums,range(1,len(nums)+1)):
            print(i,j)
            if i!=j:
                if j not in nums:
                  a.append(j)
                  break
        return a        
