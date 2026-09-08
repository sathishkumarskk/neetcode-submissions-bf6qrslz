class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        main=[]
        for i in emails:
            s=list(i)
            while "." in i and s.index(".")<s.index("@"):
                    s=list(i)
                    s.remove(".")
                    i="".join(s)
                    s=list(i)
            while "+" in i:
                i1=i.index("+")
                j=i.index("@")
                del s[i1:j]
                i="".join(s)
            main.append(i)
        return len(set(main))        
                
                        
                        
        