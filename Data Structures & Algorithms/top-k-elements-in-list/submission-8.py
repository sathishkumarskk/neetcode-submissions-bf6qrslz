class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=nums
        n.sort()#sorted and contain duplicate
        s=set(n)
        sett=list(s)#remove duplicate
        sett.sort()
        se=sett[::-1]
        count=[]
        output=[]
        if len(sett)==k:
            return(sett)
        else:    
            for i in range(0,len(se)):
                c=n.count(se[i])
                count.append(c)
            for i in count:
                maxi=max(count)
                output.append(se[count.index(maxi)])
                se.pop(count.index(maxi))
                count.remove(maxi)
                if len(se)==2:
                    maxi=max(count)
                    output.append(se[count.index(maxi)])
                    se.pop(count.index(maxi))
                    count.remove(maxi)
            output.append(se[0])         
            return(output[0:k])        