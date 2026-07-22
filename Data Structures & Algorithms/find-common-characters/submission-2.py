class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a=words[0]
        a=list(a)
        b=[]
        for i in a[:]:
            c=0
            for j in words[:]:
                if i in j:
                    indexx=words.index(j)
                    l=list(j)
                    l.remove(i)
                    words[indexx]=l
                    c+=1
                    if c==len(words):
                        b.append(i)
                        c=0
                else:
                    c=0
        return list(b)                           
            

        