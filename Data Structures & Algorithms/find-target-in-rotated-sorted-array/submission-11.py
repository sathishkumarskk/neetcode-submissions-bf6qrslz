class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and target!=nums[0]:
            return -1
        if len(nums)==1 and target==nums[0]:
            return 0            
        l1=0
        r1=0
        while r1+1<len(nums):
            if nums[r1]<nums[r1+1]:
               r1+=1
            else:
                break   
        copyy=r1    
        while l1<=r1:
            mid=(l1+r1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l1=mid+1
            else:
                r1=mid-1
        l2=copyy+1
        r2=len(nums)-1
        print(" l2:",l2)
        print(" r2:",r2)
        while l2<=r2:
            mid=(l2+r2)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l2=mid+1
            else:
                r2=mid-1   
        return -1                 