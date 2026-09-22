class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
#            print(nums[mid-1],"<-",nums[mid],"->",nums[mid+1])
            if mid==len(nums)-1 or nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            else:
                if nums[mid]==nums[mid+1]:
                    print("IF")
                    if len(nums[i:mid])%2!=0:
                       print("--if--") 
                       j=mid-1
                    else:
                        print("--else--")
                        i=mid+2
                else:
                    print("ELSE")
                    print(nums[i:mid],nums[mid],nums[mid+1:j+1])
                    if len(nums[mid+1:j+1])%2!=0: 
                        print("--if--")
                        i=mid+1
                    else:
                        print("--else--")
                        j=mid       





        