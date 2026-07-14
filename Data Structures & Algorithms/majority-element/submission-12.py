class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        e=0
        for i in nums:
            if nums.count(i)>a:
                a=nums.count(i)
                e=i
        return e       
        