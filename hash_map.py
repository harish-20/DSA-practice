class HashedTable:
    def __init__(self, MAX):
        self.MAX = MAX
        self.values = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        hashed_key = 0
        for letter in key:
            hashed_key += ord(letter)
        hashed_key = hashed_key % self.MAX

        return hashed_key
    
    def __setitem__(self, name, value):
        hashed_key = self.get_hash(name)
        self.values[hashed_key] = value
        pass

    def __getitem__(self, name):
        hashed_key = self.get_hash(name)

        return self.values[hashed_key]
    
    def __delitem__(self, name):
        hashed_key = self.get_hash(name)
        self.values[hashed_key] = None
    
    def get_all(self):
        for item in self.values:
            print(item)

expenses = HashedTable(30)

expenses['march 12'] = 100
print(expenses['march 12'])

expenses['march 13'] = 300
print(expenses['march 13'])

del expenses['march 13'] 
print(expenses['march 13'])

# expenses.get_all()