class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        i=0
        while(i<len(logs)):
            if logs[i]=="../":
                if count>0:
                    count-=1   
#                print("if")
                i+=1
            elif logs[i]=="./":
                i+=1  
#                print("elif") 
                pass  
            else:
                count+=1
                i+=1
#                print("else")
            print("count:",count)                
        if count<=0:
            return(0)
        else:            
            return(count)        
