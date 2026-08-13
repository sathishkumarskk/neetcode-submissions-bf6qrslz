class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print("sort:",nums)
        a=nums[:k]
        main=[]
        if k==len(nums):
            main.append(max(a)-min(a))
        for j in range(k,len(nums)):
            print("hi")
            main.append(max(a)-min(a))    
            a.append(nums[j]) 
            a.pop(0) 
            if j==len(nums)-1:
                main.append(max(a)-min(a))       
        if len(main)==0:
            return 0         
        return min(main)   