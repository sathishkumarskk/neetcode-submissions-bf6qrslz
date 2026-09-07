class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       s=0
       for i in words:
        c=0
        for j in range(len(i)):
            if i[j] in chars:
                if i.count(i[j])<=chars.count(i[j]):
                  c+=1
            if j==len(i)-1:
                if c==len(i):
                    s+=c          
       return s                      
         
        