from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            res.append(s[j+1:j+num+1])
            i += num + (j-i) + 1
        return res

encoded = Solution().encode(["neet","co#de","lovelovelove","you"])
print(encoded)
print(Solution().decode(encoded))