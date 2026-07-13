class Solution:
    def isValid(self, s: str) -> bool:
        l=list()
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in '([{':
                l.append(i)
                continue
            if i not in '([{':
                if l==[]:
                    return False
                if d[i]==l[-1]:
                    l.pop()
                else:
                    return False
        if l!=[]:
            return False
        return True