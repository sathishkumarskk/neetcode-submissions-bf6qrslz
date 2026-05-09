class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=[]
        for i in arr:
            if arr.count(i)==i:
                a.append(i)
        if len(a)==0:
            return(-1)
        else:            
            return max(a)        
        