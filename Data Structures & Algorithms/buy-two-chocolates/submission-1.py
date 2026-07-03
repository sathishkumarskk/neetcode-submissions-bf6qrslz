class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if i!=j:
                    if prices[i]+prices[j]<=money:
                        a.append(prices[i]+prices[j])
        if len(a)==0:
            return money                
        return money-min(a)                

