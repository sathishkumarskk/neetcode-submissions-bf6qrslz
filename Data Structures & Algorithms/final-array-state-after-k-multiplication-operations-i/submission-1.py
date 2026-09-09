class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        c=0
        while c<k:
            mini=min(nums)
            i=nums.index(mini)
            nums[i]=mini*multiplier
            c+=1
        return nums       
            