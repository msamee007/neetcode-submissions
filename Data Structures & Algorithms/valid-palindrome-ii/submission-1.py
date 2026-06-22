class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        l=list(s)
        for i in range(len(l)):
            a=l[0:i]+l[i+1:]
            if a==a[::-1]:
                return True
        return False