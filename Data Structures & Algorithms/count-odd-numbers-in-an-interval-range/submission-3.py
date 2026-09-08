class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low=low-1
        if high%2==0:
            h=high/2
        else:
            h=(high//2)+1     
        if low%2==0:
            l=low/2
        else:
            l=(low//2)+1                  
        return round(h-l)        
        