class Solution:
    def validPalindrome(self, s: str) -> bool:
        a=list(s)
        count=0
        left=0
        right=len(a)-1
        main_count=0
        while(left<right):
            if a[left]==a[right]:
                left+=1
                right-=1
            else:
                count+=1
                break
        if count==0 or len(s)==2:
            return(True)
        else:
            for i in range(len(a)):
                c=[]            
                temp_a=a.copy()
                temp_a.pop(i)
                left=0
                right=len(temp_a)-1        
                while(left<right):
                    if temp_a[left]==temp_a[right]:
                        left+=1
                        right-=1
                        c.append(1)
                        if len(c)==((len(temp_a))//2):
                            main_count+=1
                    else:
                        c.clear()
                        break
                temp_a=a.copy()
        if main_count==0:
            return(False)
        else:
            return(True)