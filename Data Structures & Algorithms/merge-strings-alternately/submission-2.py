class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        main=[]
        for i in range(min(len(word1),len(word2))):
            main.append(word1[i])
            main.append(word2[i])
        for i in range(min(len(word1),len(word2)),max(len(word1),len(word2))):
            if len(word1)>len(word2):
              main.append(word1[i])
            else:  
              main.append(word2[i])    
        j=''.join(main)      
        return(j)        
        