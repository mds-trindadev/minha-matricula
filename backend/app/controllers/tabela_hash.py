class hash_table:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range (self.MAX)]


    def get_hash(self,key):
        h = 0
        v = 0
        a = 31415
        b = 27183
        for char in key:
            v+= ord(char)
            a = (a * b) % (self.MAX - 1)
            h = (a * h + v) % self.MAX
        
        return h 

    def setitem(self,key,val):
        h = self.get_hash(key)
        
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,val))

    def getitem(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def delitem(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]





