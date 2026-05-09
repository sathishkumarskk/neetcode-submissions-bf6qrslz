class Solution:
    def countSeniors(self, details: List[str]) -> int:
        a=0
        for i in details:
            print("loop")
#            print(int(i[11],int(i[12])
            if int(i[11]+i[12])>60:
                print("satisfy")
                a+=1
        return(a)        
        