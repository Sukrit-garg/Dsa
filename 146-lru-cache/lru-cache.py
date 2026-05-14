class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head,self.tail = Node(0,0),Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def insert_first(self,node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
    def remove(self,node):
        prev=node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert_first(self.map[key])
            return self.map[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
            self.insert_first(self.map[key])
            self.map[key].val = value
        else:
            node = Node(key,value)
            self.insert_first(node)
            self.map[key] = node
        if len(self.map)>self.cap:
            del self.map[self.tail.prev.key]
            self.remove(self.tail.prev)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)