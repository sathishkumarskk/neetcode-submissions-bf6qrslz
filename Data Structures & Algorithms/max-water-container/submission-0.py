class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=heights
        l=[]
        if len(h)==1:
            print("No possible container")
        else:    
            for i in range(0,len(h)):
                for j in range(0,len(h)):
                    if i!=j:
                        height=min(h[i],h[j])
                        width=abs(i-j)
                        area=height*width
                        l.append(area)
        return(max(l))                    
        