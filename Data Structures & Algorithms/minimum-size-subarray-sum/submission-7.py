class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a=[]
        main=[]
        for j in range(len(nums)):
            a.append(nums[j])
            while sum(a)>=target:
                main.append(len(a))
                a.pop(0)
        if len(main)==0:
            return 0        
        return min(main)        


        