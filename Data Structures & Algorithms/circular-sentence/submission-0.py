class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
          if sentence[0]!=sentence[-1]:
            return False
          a=sentence.split()
          i=0
          j=1
          while j<len(a):
            if a[i][-1]!=a[j][0]:
                return False
            i+=1
            j+=1
          return True  

