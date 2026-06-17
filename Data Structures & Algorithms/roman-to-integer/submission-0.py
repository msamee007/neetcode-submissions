class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s1=0
        i=0
        while i<len(s):
         try:
            if s[i]=='I' and s[i+1] in 'XV':
                if s[i+1]=='V':
                    s1+=4
                else:
                    s1+=9
                i+=2
                continue
            elif s[i]=='X' and s[i+1] in 'LC':
                if s[i+1]=='L':
                    s1+=40
                else:
                    s1+=90
                i+=2
                continue
            elif s[i]=='C' and s[i+1] in 'DM':
                if s[i+1]=='D':
                    s1+=400
                else:
                    s1+=900
                i+=2
                continue
         except:
            pass
         s1+=d[s[i]]
         i+=1
        return s1