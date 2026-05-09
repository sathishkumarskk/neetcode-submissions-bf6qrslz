class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=""
        i=0
        j=0
        while(i<len(word1) and j<len(word2)):
          a+=word1[i]
          a+=word2[j]
          i+=1
          j+=1        
        if len(word1)>len(word2):
          a+=word1[j:len(word1)]
        else:        
          a+=word2[i:len(word2)]  
        return(a)          


        