class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while True:
            a = s[p1].lower()
            b = s[p2].lower()
            if p1 >= p2:
                return True
            
            if not a.isalnum():
                p1 += 1
                continue
            if not b.isalnum():
                p2 -= 1
                continue

            if a == b:
                p1 += 1
                p2 -= 1
            else:
                return False


print(Solution().isPalindrome("ab_a"))