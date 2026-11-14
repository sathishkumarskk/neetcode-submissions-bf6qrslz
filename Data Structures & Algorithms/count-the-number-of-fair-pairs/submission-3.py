class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count(target):
            left = 0
            right = len(nums) - 1
            ans = 0

            while left < right:
                if nums[left] + nums[right] <= target:
                    ans += right - left
                    left += 1
                else:
                    right -= 1

            return ans

        return count(upper) - count(lower - 1)