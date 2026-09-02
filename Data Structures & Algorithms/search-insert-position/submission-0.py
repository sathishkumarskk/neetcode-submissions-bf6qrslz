class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)
        print("list:",nums)
        while l<=r:
            mid=(l+r)//2
            print("mid:",mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
                if l>=len(nums):
                    return l
            else:
                r=mid-1 
   
        return l                
        