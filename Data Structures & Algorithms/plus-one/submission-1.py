class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        a=int(s)+1
        l=[]
        while a!=0:
            l.append(a%10)
            a=a//10
        return l[::-1]