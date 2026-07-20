class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            m1=max(stones)
            stones.remove(max(stones))
            m2=max(stones)
            stones.remove(max(stones))
            a=abs(m1-m2)
            stones.append(a)
        if len(stones)==0:
            return 0
        return stones[0]        
        