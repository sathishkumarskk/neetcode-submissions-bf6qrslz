class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in operations:
            try:
                int(i)
                a.append(int(i))
            except:    
                    if i=="C":
                        a.pop()
                    elif i=="+":
                        a.append(a[-1]+a[-2])
                    else:
                        a.append(2*a[-1])     
        return(sum(a))               
 