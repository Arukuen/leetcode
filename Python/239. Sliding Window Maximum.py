from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes = deque(nums[0])
        start = end = 0
        output = []

        for i in range(1, len(nums) - k):
            while end - start < k:
                pass
                


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))