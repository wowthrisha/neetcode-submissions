class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        #t=[0]*n
        ps=list(zip(position,speed))
        ps.sort(key = lambda x:x[0],reverse=True)
        f=1
        pft=0
        for p,s in ps:
            t=(target-p)/s 
            if p==ps[0][0]:
                pft=t
            if pft<t:
                f+=1
                pft=t
            
   
        
        return f
        
