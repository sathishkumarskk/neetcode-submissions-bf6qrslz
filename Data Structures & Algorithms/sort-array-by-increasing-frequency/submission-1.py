class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s=sorted(set(nums))
        count=[nums.count(i) for i in s]
        s=s[::-1]
        count=count[::-1]
        s1=[]
        count1=[]
        mini=min(count)
        while len(count)!=0:
            for i in range(len(count)):
                if count[i]==mini:
                    count1.append(count[i])
                    s1.append(s[i])
                    count.remove(count[i])
                    s.remove(s[i])
                    if len(count)!=0:
                        mini=min(count)
                    break
        s=s1
        count=count1    
        main=[]
        z=0
        mini=min(count)
        while len(count)!=0:
            for i in range(len(count)):
                if count[i]==mini:
                    for j in range(count[i]):
                        if z==0:
                            element=s[i]
                            main.append(s[i]) 
                    z+=1                  
            if len(count)!=0:        
                count.remove(mini)
                s.remove(element) 
            if len(count)!=0:    
               mini=min(count) 
            z=0               
        return(main)          
