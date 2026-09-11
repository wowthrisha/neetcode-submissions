class Solution:
    

        
    def rob(self, nums: List[int]) -> int:
        #skip 1st - clockwise 
        n=len(nums)
        def skip1(nums):
            c=0
            a=len(nums)
            l,r=0,nums[0]
            for i in range(1,a):
                c=max(r,nums[i]+l)
                l=r
                r=c
            return r
        if n==1:
            return nums[0]
        a1n=nums[1:n]
        a1=skip1(a1n)
        aln=nums[0:n-1]
        al=skip1(aln)
        return max(a1,al)