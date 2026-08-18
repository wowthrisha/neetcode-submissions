class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,cur=[],[]
        def dfs(i):
            if i==len(s):
                res.append(cur.copy())
                return
            for j in range(i,len(s)):
                c=s[i:j+1]
                if c==c[::-1]:
                    cur.append(c)
                    dfs(j+1) #nxt chararcher
                    cur.pop()
        dfs(0)
        return res
                

            


