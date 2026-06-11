class Solution:
    def isHappy(self, n: int) -> bool:
        d=[]
        while True:
            s=0
            while n!=0:
                x=(n%10)**2
                s=s+x
                n//=10
            if s not in d:
                d.append(s)
            elif s in d:
                return False
            if s==1:
                return True
            else:
                n=s
        
    