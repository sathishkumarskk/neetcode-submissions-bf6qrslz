class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    a+=prices[j]-prices[i]
                break
        return a            

