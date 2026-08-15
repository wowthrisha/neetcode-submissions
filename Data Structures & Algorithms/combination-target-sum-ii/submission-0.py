class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a=[]
        candidates.sort()
        def dfs(start,r):
            if r==0:
                a.append(c.copy())
                return     
            for i in range(start,len(candidates)):
                if candidates[i]>r:
                    break
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                c.append(candidates[i])
                dfs(i+1,r-candidates[i])
                c.pop()
        c=[]
        dfs(0,target)
        return a
                
