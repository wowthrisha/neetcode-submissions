class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm,tm={},{}
        if len(s)!=len(t):
            return False
        for si in s:
            sm[si]=sm.get(si,0)+1
        for ti in t:
            tm[ti]=tm.get(ti,0)+1
        sorted(sm)
        sorted(tm)
        print(sm)
        print(tm)
        if sm==tm:
            return True
        else :
            return False