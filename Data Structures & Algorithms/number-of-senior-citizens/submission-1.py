class Solution:
    def countSeniors(self, details: List[str]) -> int:
        a=0
        for i in details:
            if int(i[11]+i[12])>60:
                print("satisfy")
                a+=1
        return(a)        
        