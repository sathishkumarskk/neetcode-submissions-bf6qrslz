class Solution:
    def maxDepth(self, s: str) -> int:
        a=[]
        c=0
        main=0
        for i in s:
            if i=="(" or i==")":
                a.append(i)
        print(a)        
        for i in a:
            print("c:",c)
            if i=="(":
                c+=1
            else:
                main=max(main,c)                
                c-=1
        return main                    
        