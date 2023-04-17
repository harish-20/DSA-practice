class BinaryTree:
    def __init__(self, data):
        self.data = data

        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
    
    def search_element(self, element):
        if self.data == element:
            return True
        
        if element < self.data:
            if self.left:
                return self.left.search_element(element)
            else:
                return False

        if element > self.data:
            if self.right:
                return self.right.search_element(element)
            else:
                return False

    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()
        
        return elements

numberTree = BinaryTree(15)

numberTree.addChild(10)
numberTree.addChild(30)
numberTree.addChild(60)
tree = numberTree.inorder_traversal()
print(tree)

print(numberTree.search_element(10))
print(numberTree.search_element(90))
        