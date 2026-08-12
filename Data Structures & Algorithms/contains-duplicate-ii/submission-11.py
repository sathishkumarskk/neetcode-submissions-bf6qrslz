class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        w=set()
        for j in range(len(nums)):
            while j-i>k:
                w.remove(nums[i])
                i+=1
            if nums[j] in w:
                return True
            w.add(nums[j])
        return False                