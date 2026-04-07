class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = strs
        l=[len(i) for i in w]
        mini=min(l)
        store=[]
        c=0
        for i in range(mini):
            word=w[0][i]
            for j in range(len(w)):
                if w[j][i]==word:
                    c+=1
            if c==len(w):
                store.append(word)
                c=0
            else:
                break
        a="".join(store)
        return a