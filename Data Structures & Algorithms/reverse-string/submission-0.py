class Solution:
    def reverseString(self, s: List[str]) -> None:
        half=int(len(s)/2)
        for f,l in zip(range(half),range(len(s)-1,half-1,-1)):
            print(f,l)
            s[f],s[l]=s[l],s[f]       
        