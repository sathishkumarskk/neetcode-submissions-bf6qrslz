class Solution:
    def maxDepth(self, s: str) -> int:
        a=[]
        c=0
        main=0
        for i in s:
            if i=="(" or i==")":
                a.append(i)       
        for i in a:
            if i=="(":
                c+=1
            else:
                main=max(main,c)                
                c-=1
        return main                    
        