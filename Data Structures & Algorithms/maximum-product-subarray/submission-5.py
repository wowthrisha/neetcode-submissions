class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        m=nums[0]
        p,s=0,0
        for i in range(n):
            # if p is true then p else 1
            p=(p or 1)*nums[i] 
            s=(s or 1)*nums[-1-i]
            m=max(p,s,m)
        return m
        