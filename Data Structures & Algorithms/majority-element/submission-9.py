class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=list(set(nums))
        count=[]
        for i in m:
            count.append(nums.count(i))
        return(m[count.index(max(count))])