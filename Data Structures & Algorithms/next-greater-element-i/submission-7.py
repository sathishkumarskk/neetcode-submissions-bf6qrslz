class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums1)):
            c=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                   for k in range(j+1,len(nums2)):
                    if c==0:
                        if nums2[k]>nums1[i]:
                            a.append(nums2[k])
                            c+=1
                if j==len(nums2)-1 and c==0:
                    a.append(-1)
        return a