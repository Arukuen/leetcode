class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s not in hash:
                hash[s] = [str]
            else:
                hash[s].append(str)
        return hash.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))