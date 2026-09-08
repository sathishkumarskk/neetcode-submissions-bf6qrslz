class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if k>=len(arr):
            return ""
        a=[]
        for i in arr:
            if arr.count(i)==1:
                a.append(i) 
        print("a:",a)        
        if k-1>=len(a):
            return ""   
        if len(a)==0:
            return ""       
        return a[k-1]             
        