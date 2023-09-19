from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = set()
        for n in nums:
            if n in hash:
                return n
            hash.add(n)


print(Solution().findDuplicate([1,3,4,2,2]))