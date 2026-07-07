class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        for i in arr2:
            for j in range(arr1.count(i)):
                a.append(i)
                arr1.remove(i)
        arr1.sort()
        return a+arr1        
                