class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=[]
        for i in range(len(words)):
            for j in range(len(words)):
                print(i,j)
                if len(words[i])<len(words[j]):
                    if words[i] in words[j]:
                        if words[i] not in a:
                           a.append(words[i])
        return(a)                
        