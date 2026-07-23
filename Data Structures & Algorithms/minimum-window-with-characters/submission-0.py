class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        c,w={},{}
        l=0
        ans,anslen=[-1,-1],float("infinity")

        for i in range(len(t)):
            c[t[i]]=1+c.get(t[i],0)
        h,n=0,len(c)
        for r in range(len(s)):
            a=s[r]
            w[a]=1+w.get(a,0)
            if a in c and c[a]==w[a]:
                h+=1
            while h==n:
                d=r-l+1
                if anslen>d:
                    ans=[l,r]
                    anslen=d

                b=s[l]
                w[b]-=1
                if b in c and w[b]<c[b]:
                    h-=1
                l+=1
                
        l,r=ans
        return s[l:r+1] if anslen!=float("infinity") else ""
        