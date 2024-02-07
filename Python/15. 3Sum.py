from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        prev = None
        for p0 in range(len(nums)):
            if p0 + 3 > len(nums):
                break
            if nums[p0] == prev:
                continue
            prev = nums[p0]
            p1 = p0 + 1
            p2 = len(nums) - 1
            while True:
                if p1 >= p2:
                    break
                sum = nums[p0] + nums[p1] + nums[p2]
                if sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    output.append([nums[p0], nums[p1], nums[p2]])
                    p2 -= 1
                    p1 += 1
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
        return output
    
print(Solution().threeSum([-2,0,0,2,2]))
                