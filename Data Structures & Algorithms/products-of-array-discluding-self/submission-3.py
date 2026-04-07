class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = nums
        l = n
        total = 1
        totall = 1
        newlist = []
        zero_count = 0

        for i in l:
            if i == 0:
                zero_count += 1
            else:
                continue

        for p in l:
            if p == 0:
                continue
            else:
                mult = p * totall
                totall = mult

        for i in l:
            mul = i * total
            total = mul

        for i in l:
            if zero_count > 1:
                newlist.append(0)
            else:
                if i == 0:
                    newlist.append(totall)
                else:
                    result = int(total / i)
                    newlist.append(result)

        return(newlist)        