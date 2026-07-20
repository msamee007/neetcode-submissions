class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i[-1].isdigit():
                l.append(int(i))
            else:
                a,b=l.pop(),l.pop()
                if i =='+':
                    l.append(a+b)
                elif i=='-':
                    l.append(int(b-a))
                elif i=='*':
                    l.append(a*b)
                elif i=='/':
                    l.append(int(float(b)/a))
        return l[0]