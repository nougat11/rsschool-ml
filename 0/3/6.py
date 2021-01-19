class Vector:
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)
    
    def add(self, other):
        if (len(self) != len(other)):
            raise Exception("sad")
        list=self.list[:]
        for i in range(len(other)):
            list[i]+= other.list[i]
        print(list)
        return Vector(list)
    
    def subtract(self, other):
        if (len(self) != len(other)):
            raise Error("sad")
        print(self.list)
        list=self.list[:]
        for i in range(len(other)):
            list[i]-= other.list[i]
        print(self.list)
        return Vector(list)
    
    def dot(self, other):
        if (len(self) != len(other)):
            raise Error("sad")
        k = 0
        for i in range(len(other)):
            k+=self.list[i] * other.list[i]
        print(k)
        return k
    
    def norm(self):
        
        k = 0
        for i in range(len(self)):
            k+=self.list[i] **2
        print(k)
        return k **0.5
    
        
    
    def equals(self, other):
        if (self.list == other.list):
            return True
        else:
            return False
    def __str__(self):
        list1 = self.list[:]
        list1 = list(map(str, list1))
        return '(' + ",".join(list1) +')'
        
            
