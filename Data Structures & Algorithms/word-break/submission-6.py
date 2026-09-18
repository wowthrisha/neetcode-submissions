class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m={}
        def dfs(i):
            if i==len(s):
                return True
            if i in m:
                return m[i]
            for w in wordDict:
                if len(w)+i<=len(s) and s[i:i+len(w)]==w:
                    m[i]=True
                    if dfs(len(w)+i):
                        return True
            m[i]=False   
            return False
            
        return dfs(0)
                
                
            
                
