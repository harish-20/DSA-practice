class HashedTable:
    def __init__(self, MAX):
        self.MAX = MAX
        self.values = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hashed_key = 0
        for letter in key:
            hashed_key += ord(letter)
        hashed_key = hashed_key % self.MAX

        return hashed_key
    
    def __setitem__(self, name, value):
        hashed_key = self.get_hash(name)

        found = False
        for index, element in enumerate(self.values[hashed_key]):
            if element[0] == name:
                self.values[hashed_key][index] = (name, value)
                found = True

        if not found:
            self.values[hashed_key].append((name, value))
        

    def __getitem__(self, name):
        hashed_key = self.get_hash(name)
        for element in self.values[hashed_key]:
            if element[0] == name:
                return element[1]

    
    def __delitem__(self, name):
        hashed_key = self.get_hash(name)
        for index, element in enumerate(self.values[hashed_key]):
            if element[0] == name:
                del self.values[hashed_key][index]
    
    def get_all(self):
        for item in self.values:
            print(item)

expenses = HashedTable(10)

expenses['march 7'] = 100
print(expenses['march 7'])

expenses['march 18'] = 110
print(expenses['march 18'])

del expenses['march 18']
print(expenses['march 18'])

expenses['march 4'] = 600
expenses['march 15'] = 200
expenses['march 24'] = 200
expenses.get_all()

del expenses['march 24']
expenses.get_all()

expenses['march 4'] = 300
print(expenses['march 4'])
expenses.get_all()
