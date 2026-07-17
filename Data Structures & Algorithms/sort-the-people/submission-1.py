class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=[]
        for i in range(len(names)):
            a.append([heights[i],names[i]])
        print("a:",a)    
        a.sort()
        print("a:",a)
        b=[]
        for i in range(len(a)-1,-1,-1):
            b.append(a[i][1])
        return b   