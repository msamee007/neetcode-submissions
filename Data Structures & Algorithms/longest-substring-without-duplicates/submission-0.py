class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" ":
            return 1
        s1=0
        l=0
        k=""
        for i in s:
            k+=i
            if len(k)==len(set(k)):
                l+=1
            else:
                while i in k:
                    k = k[1:]
                    if len(k)==len(set(k)):
                        break
                l=len(k)
            s1=max(s1,l)
        return s1