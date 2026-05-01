class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=len(needle)-1
        a=[]
        while(j<len(haystack) and i<len(haystack)):
            if len(needle)==1:
                if haystack[i]==needle:
                    return(i)
                else:
                    i+=1    
            else:
                if haystack[i:j+1]==needle:
                    return(i)                  
                i+=1
                j+=1
        return(-1)        