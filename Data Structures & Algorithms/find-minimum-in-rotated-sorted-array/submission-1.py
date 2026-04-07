class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = nums
        l = n
        min = l[0]
        for i in l:
            if i < min:
                min = i
        return( min)        