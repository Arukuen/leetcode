from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if n-1 not in nums_set:
                l = 1
                while n+l in nums_set:
                    l += 1
                longest = max(longest, l)
        return longest
    
print(Solution().longestConsecutive([100,4,200,1,3,2]))