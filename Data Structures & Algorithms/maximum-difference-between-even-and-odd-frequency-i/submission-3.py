class Solution:
    def maxDifference(self, s: str) -> int:
        odd=[]
        even=[]
        for i in set(s):
            if s.count(i)%2==0:
                even.append(s.count(i))
            else:
                odd.append(s.count(i))
        return max(odd)-min(even)          
        