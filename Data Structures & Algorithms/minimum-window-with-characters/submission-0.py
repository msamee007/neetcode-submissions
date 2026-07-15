from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        count = {}

        matched = 0
        required = len(target)

        left = 0
        start = -1
        minLen = float("inf")

        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1

            if ch in target and count[ch] == target[ch]:
                matched += 1

            while matched == required:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                count[s[left]] -= 1

                if s[left] in target and count[s[left]] < target[s[left]]:
                    matched -= 1

                left += 1

        if start == -1:
            return ""

        return s[start:start + minLen]