class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        main=[]
        a=nums1+nums2
        for i in range(len(a[:])):
            for j in range(i+1,len(a[:])):
                if a[i]!=0 and a[j]!=0:
                    if a[i][0]==a[j][0]:
                        a[i]=[a[i][0],a[i][1]+a[j][1]]
                        a[j]=0
    #                    main.append([a[i][0],a[i][1]+a[j][1]])
        return sorted([i for i in a if i!=0])           
                    
            

