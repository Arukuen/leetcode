from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []
        for window in range(len(str(low)), len(str(high)) + 1):
            for w in range(0, 10-window):
                temp = (int(''.join(map(str, list(range(w+1, w + 1 + window))))))
                if low <= temp and temp <= high:
                    output.append(temp)
        return output


Solution().sequentialDigits(1000, 13000)