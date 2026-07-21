import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i=0
        c=0
        while(i<k):
            maxi=max(gifts)
            gifts[gifts.index(maxi)]=int(math.sqrt(maxi))
            i+=1   
        return sum(gifts)            

        
        