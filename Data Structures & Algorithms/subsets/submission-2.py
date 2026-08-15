class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        s=[]
        def dfs(i):
            #append to res on reaching leaf of each path
            if i>=len(nums):
                r.append(s.copy())
                return
            #LST: include i
            s.append(nums[i])
            #go deeper
            dfs(i+1)
            #RST: exclude i
            s.pop()
            dfs(i+1)
        #initial
        dfs(0)
        return r