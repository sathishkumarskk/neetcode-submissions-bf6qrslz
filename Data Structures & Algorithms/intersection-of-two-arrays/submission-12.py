class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        a=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                if nums1[i] not in a:
                    a.append(nums1[i])
                    i+=1
            j+=1
            if j>len(nums2)-1:
                j=0
                i+=1        
        return(a)            
