class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        while i<len(word) or j<len(abbr):
            if i>=len(word):
                 return False 
            if word[i]==abbr[j]:               
                i+=1
                j+=1
            elif word[i]!=abbr[j] and abbr[j].isalpha():
                return False
            else:

                if abbr[j].isdigit():
                    s=""
                    while j<len(abbr) and abbr[j].isdigit():
                        s+=abbr[j]
                        j+=1
                    i+=int(s)                        
                    if s[0]=="0":
                        return False 
                    if i>len(word):
                        return False      
                    print("s:",s)                     
                    s="" 
        print("i:",i)
#        if i>len(word):
#            return False
        return True            

        