class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=len(needle)
        k=0
        print(len(haystack))
        if haystack==needle:
            return 0
        while(j<=len(haystack) and k<len(haystack)):
            if len(needle)==1:
                print("iff")
                if haystack[k]==needle:
                    return k
                else:
                    k+=1  
            else:          
                print(haystack[i:j],needle)
                print(i,j)
                if haystack[i:j]==needle:
                    print("eqal")
                    return i
                i+=1
                j+=1
        return -1        