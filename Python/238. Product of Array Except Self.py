from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        dp1 = length * [1]
        dp2 = length * [1]

        for i in range(1, length):
            dp1[i] = dp1[i-1] * nums[i-1]

        for i in range(length - 2, -1, -1):
            dp2[i] = dp2[i+1] * nums[i+1]

        return [dp1[i] * dp2[i] for i in range(length)]

print(Solution().productExceptSelf([1,2,3,4]))