class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create empty lists for len(i/p_list)
        #each elemnt nd its freq
        f=[[] for i in range(len(nums)+1)]
        #map char to f
        c={}
        for n in nums:
            #find f of each n in nums
            c[n]=1+c.get(n,0)
        print("c:",c)
        #map index number of list to frequencey of occurance and thus resp elemnets
        for n,c in c.items():
            f[c].append(n)
            #print(f'{n}n,{c}c,{f[c]}')
            
        #print("f:",f)
        r=[]
        for i in range(len(f)-1,0,-1):
            ##print("r:",r)
            #traverse bucket f and at each index i chk, the stores lements with the freq i
            #add value with freq i to result where len(r)==k is returned
            for n in f[i]:
                r.append(n)
                #print("r=",r)
                if len(r)==k:
                    return r
    
        

            


                
