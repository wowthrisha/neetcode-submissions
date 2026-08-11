class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        node.next=self.right
        node.prev=prev
        self.right.prev=node
    def remove(self,node):
        next=node.next
        prev=node.prev
        prev.next=next
        next.prev=prev
        

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        #move to mru
    
        
        return node.value


        
    def put(self, key: int, value: int) -> None: 
        
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
           
            node.value=value
            self.insert(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)       
            del self.cache[lru.key]

        
