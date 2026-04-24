class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        for i in range(len(temperatures)):
            c=0
            for j in range(i,len(temperatures)):
               if c==0:
                    if i!=j:
                        if temperatures[i]<temperatures[j]:
                            a.append(abs(i-j))
                            c+=1
                            break
               if c==0 and j==len(temperatures)-1:
                  a.append(0)     

        return(a)            
        