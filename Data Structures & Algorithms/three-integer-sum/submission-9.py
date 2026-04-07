class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=nums
        l=[]
        for i in range(0,len(n)):
            for j in range(0,len(n)):
                for k in range(0,len(n)):
                    if i!=j and j!=k and k!=i:
                        if n[i]+n[j]+n[k]==0:
                            li=[]
                            li.append(n[i])
                            li.append(n[j])
                            li.append(n[k])
                            li.sort()
                            l.append(li)
        t=map(tuple,l)
        s=set(t)
        lis=map(list,s)
        listtu=list(lis)
        return(listtu)        