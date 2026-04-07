class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = nums
        l = n
        found = 0
        for i in n:
            for j in n:
                if i == j:
                    found += 1
                else:
                    found += 0
        if found > len(l):
            return True
        else:
            return False        
        