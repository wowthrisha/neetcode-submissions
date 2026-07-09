class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        c={}
        mf=0
        for r in range(len(s)):
            
            c[s[r]]=1+c.get(s[r],0)
            mf=max(c[s[r]],mf)
            while (r-l+1)-mf>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res