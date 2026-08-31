class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            return -1    
        left=0
        right=len(nums)
        while left<=right:
            mid=(left+right)//2
            if left>=len(nums) or right<0:
                return -1
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1                
        return -1                
        