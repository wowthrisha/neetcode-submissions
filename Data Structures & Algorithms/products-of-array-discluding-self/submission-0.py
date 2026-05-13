class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[1]*n
        pre=1
        for i in range(n):
            r[i]=pre
            pre*=nums[i]
        post=1
        for i in range(n-1,-1,-1):
            r[i]*=post
            post*=nums[i]
        return r

         