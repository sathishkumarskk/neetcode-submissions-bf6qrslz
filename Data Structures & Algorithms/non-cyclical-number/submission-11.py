class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        s=0
        while(len(a)==len(set(a))):
            for i in str(n):
                print("element: ",i)
                s+=int(i)*int(i)
            a.append(s)
            print("s:",s)
            if s==1:
                return True
            n=s
            s=0
        return False            
            

        