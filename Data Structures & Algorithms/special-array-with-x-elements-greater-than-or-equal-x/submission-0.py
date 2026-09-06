class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x=[i for i in range(len(nums)+1)]
        c=0
        print("x:",x)
        main=[]
        for i in x:
            c=0
            for j in range(len(nums)):
                print("i:",i,":",nums[j])
                if i<=nums[j]:
                    c+=1
            if j==len(nums)-1:
                print("equal")
                print("x:",i)
                print("c:",c)                
                if c==i:
                    main.append(i)
#        print(main)            
        if len(main)!=0:
            return max(main) 
        return -1                   

        