class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a=nums.copy()
        a.sort()
        print("num:",nums)
        print("a:",a)
        if nums==a:
            return True
        if nums==a[::-1]:
            return True
        return False        
        