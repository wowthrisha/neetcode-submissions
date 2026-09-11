class Solution:
    def rob(self, nums: List[int]) -> int:
    
        n=len(nums)
        
      
        l,r=0,0
       
        for i in range(n):
            c=max(r,nums[i]+l)
            l=r
            r=c
        return r
