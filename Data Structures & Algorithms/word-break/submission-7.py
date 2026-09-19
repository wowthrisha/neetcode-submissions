class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws=set(wordDict)
        x=max(len(w) for w in ws)
        m={}
        def dfs(i):
            if i==len(s):
                return True
            if i in m:
                return m[i] 
            for j in range(i,min(len(s),x+i)):
                if s[i:1+j] in ws:
                    if dfs(j+1):
                    
                        m[i]=True
                        return True
            m[i]=False
            return False
        return dfs(0)
