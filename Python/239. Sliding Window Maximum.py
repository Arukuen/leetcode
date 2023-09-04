from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        right = 0
        output = []

        while (right < len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if queue[0] < left:
                queue.popleft()

            if right+1 >= k:
                left += 1
                output.append(nums[queue[0]])

            right += 1
    
        return output
                


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))