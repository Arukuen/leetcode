from typing import List

class Solution:
    def chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        chunked = list(self.chunks(nums, 3))
        for c in chunked:
            if max(c) - min(c) > k:
                return []
        return chunked


nums = [1,3,3,2,7,3]
k = 3

print(Solution().divideArray(nums, k))