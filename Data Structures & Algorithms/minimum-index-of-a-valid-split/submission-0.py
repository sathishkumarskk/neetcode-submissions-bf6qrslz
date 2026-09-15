class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c=0
        d=0
        for i in nums:
            if nums.count(i)>c:
                c=nums.count(i)
                d=i
        i=0
        while i<len(nums):
            left=nums[:i+1]
            right=nums[i+1:]          
            if left.count(d)>len(left)/2 and right.count(d)>len(right)/2:
                    return i
            i+=1  
        return -1                

        