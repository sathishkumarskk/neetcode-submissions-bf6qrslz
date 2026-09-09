class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        c=0
        while c<k:
            print("c:",c)
            print("k:",k)
#            print(nums)
            mini=min(nums)
#            print("mini: ",mini)
            i=nums.index(mini)
            nums[i]=mini*multiplier
            c+=1
        return nums       
            