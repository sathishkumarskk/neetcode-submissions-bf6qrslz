class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        l=[[1],[1,1]]
        if numRows==1:
            return [[1]] 
        if numRows==2:
            return [[1],[1,1]]      
        while len(l)<n:
            a=[1]
            for i in range(len(l)-1):
                a.append(l[-1][i]+l[-1][i+1])
            a.append(1)
            l.append(a)
            a=[]
        return l       