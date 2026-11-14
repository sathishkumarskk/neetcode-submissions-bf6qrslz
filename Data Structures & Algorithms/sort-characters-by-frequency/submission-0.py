class Solution:
    def frequencySort(self, s: str) -> str:
        a=[]
        for i in set(s):
            a.append([s.count(i),i])
        a.sort() 
        print("before:",a)            
        main=""
        for i in range(len(a)-1,-1,-1):
            for j in range(a[i][0]):
                main+=a[i][1]
        return main                    
              
        