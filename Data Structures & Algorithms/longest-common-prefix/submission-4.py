class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        i=0
        l=''
        while True:
            z=0
            try:
                for k in range(1,len(strs)):
                    if strs[k][i]==s[i]:
                        z+=1
                    else:
                        return l
                if z==len(strs)-1:
                    l=l+s[i]
                else:
                    return ""
                i+=1
            except IndexError:
                return l
        return l