class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        l=sorted(list(set(nums)))
        n=1
        m=1
        for i in range(len(l)-1):
            if l[i+1]==l[i]+1:
                n+=1
            else:
                n=1
            m=max(m,n)
        return m