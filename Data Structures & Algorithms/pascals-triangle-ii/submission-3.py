class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[[1],[1,1]]
        if rowIndex<=1:
            return a[rowIndex]   
        while len(a)<=rowIndex:
            main=[1]
            for i in range(len(a[len(a)-1])-1):
                main.append(a[-1][i]+a[-1][i+1])
            main.append(1)
            a.append(main)
        return a[-1]        

        