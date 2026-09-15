class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        a=[]
        for i in words:
            if i[0] in ["a","e","i","o","u"] and i[-1] in ["a","e","i","o","u"]:
                a.append(1)
            else:
                a.append(0)
        main=[]
        for i in queries:
            main.append((a[i[0]:i[-1]+1]).count(1))  
        return main             

        