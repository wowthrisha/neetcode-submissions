class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        # r = best till prev house
        r=0
        # l = best till prev.prev house
        l=0
        for i in range(n):
            # best till prev.h vs best till prev.prev.h + current
            c=max(r,l + nums[i])
            # prev.prev.h state becomes prev.h state
            l=r
            # prev.h state becomes current best
            r=c
        # return best till last house
        return r
