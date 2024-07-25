from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(99999)
        output = []
        start = nums[0]
        prev = start
        for i, num in enumerate(nums[1:]):
            if num == prev + 1:
                prev = num
            else:
                if start == prev:
                    output.append(f'{start}')
                else:
                    output.append(f'{start}->{prev}')
                if i + 1 != len(nums):
                        start = num
                        prev = num
        return output



print(Solution().summaryRanges([]))
                