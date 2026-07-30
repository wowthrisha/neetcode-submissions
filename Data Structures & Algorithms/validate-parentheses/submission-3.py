class Solution:
    def isValid(self, s: str) -> bool:
        sk=[]
        cto = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:# traverse str
            if c in cto:      #chk if its an closed bracket )]}
                if sk and sk[-1]==cto[c]: 
                #if stacjk is not empty and 
                #TOS=Value of index=(c,cto[c])==(closedb,openb)
                    sk.pop()
                #remove open bracxket once iots closed opair is found
                else:
                    return False #VIOLATED
            else:
                sk.append(c) #chk if its open bracket ([{
            
        return True if not sk else False