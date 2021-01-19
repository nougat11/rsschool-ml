class Dictionary():
    def __init__(self):
        self.d = {}
        
    def newentry(self, word, definition):
        self.d[word] = definition
        
    def look(self, key):
        if not key in self.d.keys():
            return f"Can't find entry for {key}"
        return self.d[key]
