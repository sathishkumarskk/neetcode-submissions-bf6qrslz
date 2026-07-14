class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                            c+=1
                            if nums[i]+nums[j]+nums[k]+nums[l]==target:
                                t=[nums[i],nums[j],nums[k],nums[l]]
                                t.sort()
                                if t not in a:
                                    a.append(t)
        print(c)                            
        return a                            
        