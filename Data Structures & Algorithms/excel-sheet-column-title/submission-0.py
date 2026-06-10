class Solution(object):
    def convertToTitle(self, columnNumber):
        res=''
        hmap={i: chr(64+i) for i in range(1,27)}
        
        
        while columnNumber>0:
            n=columnNumber%26
            if n==0:
                res+="Z"
                columnNumber-=1    
            else:    
                res+=hmap[n]
            columnNumber=columnNumber//26
        return (res[::-1])
        
        
        