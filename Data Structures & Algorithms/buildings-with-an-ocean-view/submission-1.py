class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:      
        stack=[]
        i=0
        main=[]
        while(i<len(heights)):
            for j in range(i+1,len(heights)):
                    if heights[j]<heights[i]:
                        stack.append(heights[j])            
            if len(stack)==len(heights[i+1:len(heights)]):
                main.append(i)
            while stack:
                stack.pop()
            i+=1           
        return main
        