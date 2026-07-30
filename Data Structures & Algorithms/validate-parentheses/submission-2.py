class Solution:
    def isValid(self, s: str) -> bool:
        sk=[]
        cto = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in cto:
                if sk and sk[-1]==cto[c]:
                    sk.pop()
                else:
                    return False
            else:
                sk.append(c)
            
        return True if not sk else False