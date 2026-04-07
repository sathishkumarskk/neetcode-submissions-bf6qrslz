class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_s=[]
        main=[]
        for i in strs:
            z=sorted(i)
            a=''.join(z)
            sort_s.append(a)
        remove_sort_s=list(set(sort_s))
        for i in remove_sort_s:
            demo=[]
            for j,e in zip(sort_s,strs):
                if i==j:
                    demo.append(e)
            main.append(demo)     
        return(main)    
            
            