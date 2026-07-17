class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a=[]
        if len(text)<7:
            return 0
        for i in ["b","a","l","l","o","o","n"]:
            if i=="l" or i=="o":
                a.append(text.count(i)//2)
            else:
                a.append(text.count(i))   
        print(a)     
        if len(a)==7:
            return min(a)    
        return 0    