class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        r=[]
        for i in range(1<<n):
            s=[nums[j] for j in range(n) if (i& (1<<j))]
            r.append(s)
        return r