class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        L = [1 for n in nums]
        for i, n in enumerate(nums):
            subprob = [L[j] if nums[j] < n else 0 for j in range(i+1)]
            L[i] = 1 + max(subprob)
        return max(L)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))