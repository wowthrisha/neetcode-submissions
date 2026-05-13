class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # i== tranverse string
        # j== work length
        #till end of string s=encoded
        while i < len(s):
            j = i
            while s[j] != '#':
                #dont stop till delimiter# is found
                j += 1
             
            #cuz j started at i and travelled till # was found 
            #length==j-i: 
            length = int(s[i:j])
            #move i to j+1 since (j-1)== len(str) -->j=i-1
            i = j + 1
            res.append(s[i:(i + length)])

            i += length

        return res