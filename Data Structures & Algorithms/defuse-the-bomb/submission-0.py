class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        main=code.copy()
        if k==0:
            return [0]*len(code)
        elif k>0:
            for i in range(len(code)):
                j=i+1
                s=0
                count=1
                while count<=k:
                    print("j:",j)
                    if j==len(code):
                        j=0
                    s+=main[j]
                    count+=1 
                    j+=1
                    print("count:",count)                    
                code[i]=s   
        else: 
            print("else")  
            for i in range(len(code)):
                j=i-1
                s=0
                count=1
                while count<=abs(k):
                    if j<0:
                        j=len(code)-1
                    s+=main[j] 
                    count+=1   
                    j-=1   
                code[i]=s   
        return code                        
