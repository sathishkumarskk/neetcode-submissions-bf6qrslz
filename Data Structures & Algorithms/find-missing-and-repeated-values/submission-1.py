class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=[]
        main=[]
        for i in grid:
            for j in i:
                a.append(j)
        for i in a:
            if a.count(i)>1:
                main.append(i)
                break
        s=sorted(set(a))
        for i,j in zip(s,range(1,s[-1]+1)):
            if i!=j:
                main.append(j)
                break   
        if len(main)==1:
            main.append(s[-1]+1)   
             
        return main             
