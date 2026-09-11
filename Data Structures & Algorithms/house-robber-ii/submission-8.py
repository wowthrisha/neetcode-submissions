class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def helper(start,end):
            l,r=0,0
            for i in range(start,end):
                c=max(r,l+nums[i])
                l=r
                r=c
            return r
        s1=helper(1,n)
        sl=helper(0,n-1)
        return max(s1,sl)