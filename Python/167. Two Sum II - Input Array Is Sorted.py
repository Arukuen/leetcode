from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while True:
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                p2 -= 1
            elif sum < target:
                p1 += 1
            else:
                return [p1+1, p2+1]

print(Solution().twoSum([2,7,11,15], 9))