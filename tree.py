class Tree():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        cursor = self

        while(True):
            if not cursor.parent:
                break
            level += 1
            cursor = cursor.parent

        return level
    
    def print_tree(self):
        gap = ' ' * 5
        prefix = gap * self.get_level() + '|__'

        print(prefix + self.data if self.get_level() else self.data)

        if(self.children):
            for child in self.children:
                child.print_tree()

electornics = Tree('Electronic')

laptops = Tree('Laptops')
electornics.add_child(laptops)

mac = Tree('mac book')
laptops.add_child(mac)
msi = Tree('MSI')
laptops.add_child(msi)
lenovo = Tree('Lenovo')
laptops.add_child(lenovo)

mobiles = Tree('Mobiles')
electornics.add_child(mobiles)

mi = Tree('MI')
mobiles.add_child(mi)
oppo = Tree('Oppo')
mobiles.add_child(oppo)
realme = Tree('Real Me')
mobiles.add_child(realme)

headphones = Tree('Headphones')
electornics.add_child(headphones)

boult = Tree('Boult')
headphones.add_child(boult)
boat = Tree('Boat')
headphones.add_child(boat)
skull_candy = Tree('Skull Candy')
headphones.add_child(skull_candy)

electornics.print_tree()