class DefaultList:
    def __init__(self, list, defa):
        self.list = list
        self.defa = defa
    
    def __getitem__(self, key):
        print(self.list, key)
        if key<len(self.list):
            if key< 0and key>=len(self.list) * (-1) or key >=0:
                return self.list[key]
            else:
                return self.defa
        else:
            return self.defa
    
    def extend(self, list):
        self.list.extend(list)
        
    def append(self, list):
        self.list.append(list)
    
    def remove(self, list):
        print(self.list)
        self.list.remove(list)
    
    def pop(self, list):
        self.list.pop(list)
    
    def insert(self, index, value):
        self.list.insert(index, value)
