class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i=0
        j=3
        a=[]
        while j<len(num)+1:
            print(num[i:j])
            if len(set(num[i:j]))==1:
                    a.append(int(num[i:j]))
            i+=1
            j+=1
        print(a)   
        if len(a)==0:
            return ""
        if a[0]==0:
                return "000"    
        return str(max(a))        

        