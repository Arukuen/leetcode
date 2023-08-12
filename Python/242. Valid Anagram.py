class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashCount = {}
        for i in range(len(s)):
            if s[i] not in hashCount: hashCount[s[i]] = 1
            else: hashCount[s[i]] += 1
            if t[i] not in hashCount: hashCount[t[i]] = -1
            else: hashCount[t[i]] -= 1
        
        for val in hashCount.values():
            if val != 0:
                return False
        return True
    
print(Solution().isAnagram("anagram", "nagaram"))