class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        i=1
        j=2
        k=3
        if n==0:
            return(True)
        else:    
            if len(flowerbed)==1:
                if flowerbed[0]==0:
                    return(True)
                else:
                    return(False)
            else:            
                if flowerbed[1]==0 and flowerbed[0]==0:
                    c+=1
                if flowerbed[-1]==0 and flowerbed[-2]==0:
                    c+=1            
                while(k<len(flowerbed)-1):
                    if flowerbed[i]==0 and flowerbed[j]==0 and flowerbed[k]==0:
                        c+=1
                        i=j+1
                        j=i+1
                        k=j+1
                    else:    
                        i+=1
                        j+=1
                        k+=1    
        print("chance: ",c)    
        if c>=n:
            return(True)
        else:
            return(False)    