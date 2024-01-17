from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 != 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
    
print(Solution().sortArrayByParity([0,2]))