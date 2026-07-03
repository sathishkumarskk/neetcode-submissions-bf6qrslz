class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=0
        for i in set(s):
            print("value: ",s.count(i))
            if s.count(i)>0 and s.count(i)%2==0:
              a+=s.count(i)
              print(s.count(i))
            else:
                if s.count(i)-1 != 0:
                    a+=s.count(i)-1  
        for j in set(s):
            if s.count(j)>0 and s.count(j)%2!=0:
                a+=1
                break
        return a        

           