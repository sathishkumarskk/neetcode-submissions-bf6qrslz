class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=heights[:]
        a.sort()
        b=0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                b+=1
        return(b)        
        