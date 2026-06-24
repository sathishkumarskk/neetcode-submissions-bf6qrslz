class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a=[]
        main=[]
        b=list(s)
        for i in b:
            if b.count(i)>1:
                a.append(i)
        if len(a)==0:
            return -1   
        print("a: ",a)         
        for z in range(len(a)):
            m=[]
            for j in range(len(b)):
               if b[j]==a[z]:
                   m.append(j)
            start=m[0]
            end=m[-1]
            main.append(len(b[start+1:end]))
            print("main: ",main)
        return max(main)            
        