class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        a1=[]
        for i in nums1:
            if i not in nums2:
                a1.append(i)
        a.append(list(set(a1))) 
        a1.clear()    
        for i in nums2:
            if i not in nums1:
                a1.append(i)  
        a.append(list(set(a1)))
        return a                              
        