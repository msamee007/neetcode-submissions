class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                    continue
            for a in range(i+1,n-2):
                if a>i+1 and nums[a]==nums[a-1]:
                    continue
                j,k=a+1,n-1
                while j<k:
                    total=nums[i]+nums[a]+nums[j]+nums[k]
                    if total==target:
                        res.append([nums[i],nums[a],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                    elif total<target:
                        j+=1
                    else:
                        k-=1
        return res
        