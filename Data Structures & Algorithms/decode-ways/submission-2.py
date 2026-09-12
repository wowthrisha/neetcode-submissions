class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        l,r=0,1
        #l=i-2=prev.prev
        #r=i-1=prev
        c=0
        for i in range(n):
            c=0
            if s[i]!='0':
                c=c+r
            if i>0 and s[i-1]!='0':
                if 10<= int(s[i-1]+s[i]) <=26:
                    c=c+l
            l=r
            r=c
        return r