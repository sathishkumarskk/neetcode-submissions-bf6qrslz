class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        c=0
        stop=0
        m=min([len(k) for k in strs])
        for i in range(len(strs)):
            if m==len(strs[i]):
                indexx=i
                break
        e=strs[indexx]
        i=0
        while i<len(e) and stop==0:
            for k in strs:
                print("compare:",e[i],k[i])
                if k[i]==e[i]:
                    c+=1 
                else:
                    stop+=1             
            if c==len(strs):
                print("if")
                print("count:",c)
                s+=e[i]
            c=0  
            i+=1       
        return s                                         


            
        