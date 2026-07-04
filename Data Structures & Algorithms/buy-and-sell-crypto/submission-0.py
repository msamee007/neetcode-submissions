class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float('inf')
        s=0
        for i in prices:
            if i<m:
                m=i
            s=max(s,i-m)
        return s