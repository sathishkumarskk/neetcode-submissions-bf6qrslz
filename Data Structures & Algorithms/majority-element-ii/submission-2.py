class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m=list(set(nums))
        count=[]
        l=[]
        mod=len(nums)//3
        for i in m:
            count.append(nums.count(i))
        for e,c in zip(m,count):
            if nums.count(e)>mod:
                l.append(e)
        return(l)         