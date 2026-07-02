class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:      
        stack=[]
        i=0
        main=[]
        while(i<len(heights)):
            for j in range(i+1,len(heights)):
                if len(stack)==0:
                    if heights[j]>=heights[i]:
                        stack.append(heights[j])            
            if len(stack)==0:
                main.append(i)
            if len(stack)!=0:    
               stack.pop()    
            i+=1           
        return main
        