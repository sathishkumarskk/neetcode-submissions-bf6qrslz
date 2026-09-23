class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if (nums[mid]==nums[mid+1] or nums[mid]==nums[mid-1]):
                return nums[mid]
            else:
                if len(nums[i:mid+1])==len(set(nums[i:mid+1])):
                    i=mid+1
                else:
                    j=mid-1    
