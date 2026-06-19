class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i].isalnum()!=True:
                i+=1
            elif s[j].isalnum()!=True:
                j-=1
            else:
                if s[i].lower()==s[j].lower():
                    pass
                else:
                    return False
                i+=1
                j-=1
        return True