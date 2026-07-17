class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=heights.copy()
        a.sort()
        c=0
        for i in range(len(a)):
            if a[i]!=heights[i]:
                c+=1
        return c        
        