class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        l=list(s)
        for i in range(len(l)):
            a=l[i]
            l.pop(i)
            if l==l[::-1]:
                return True
            else:
                l.insert(i,a)
        return False
