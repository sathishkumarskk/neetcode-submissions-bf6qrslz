class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        b=[]
        a=0
        for i in nums:
            if i==1:
                a+=1
                print(a)   
            else:
                b.append(a)
                a=0
        b.append(a)
        return(max(b))        

        