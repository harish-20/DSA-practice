class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0

        itre = self.head
        while(itre.next):
            length += 1
            itre = itre.next
        return length

    def is_valid_index(self, index):
        if(index < 0 or index >= self.get_length()):
            return False
        return True

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_index(self, value, index):
        length = self.get_length()
        if(not self.is_valid_index(index)):
            raise Exception('Index out of bound')

        node= Node(value)
        itre = self.head
        for cursor in range(length):
            if(cursor == index-1):
                node.next = itre.next.next
                itre.next = node
                break
            itre = itre.next

    def insert_at_end(self, value):
        node = Node(value)

        itre = self.head
        while(itre.next is not None):
            itre = itre.next
        itre.next = node

    def remove_at_first(self):
        self.head = self.head.next

    def remove_at_last(self):
        length = self.get_length()
        if(length == 0):
            raise Exception('List is empty')

        if(length == 1):
            self.head = None
            return

        itre = self.head
        while(itre.next.next):
            itre = itre.next
        itre.next = None

    def remove_at_index(self, index):
        length = self.get_length()
        if(length == 0):
            raise Exception('List is empty')

        if(length == 1):
            self.head = None
            return

        length = self.get_length()
        if(not self.is_valid_index(index)):
            raise Exception('Index out of bound')
        
        itre = self.head
        for cursor in range(length):
            if(cursor == index):
                itre.next = itre.next.next
                break
    
    def print_elements(self):
        node = self.head
        
        result = ''
        while(node):
            result += ' --> '+ node.data
            node = node.next

        print(result)

movies = LinkedList()

while(True):
    movies.print_elements()
    option = int(input(
        """
        Enter the operation to do
        options
        1: insert at begining
        2: insert at end
        3: insert at some specific position(index start from 0)
        4: remove first
        5: remove end
        6: remove specific element(index start from 0)
        7: get length
        0: exit
        """
        ))
    if(option == 0):
        break
    else:
        match option:
            case 1:
                value = input('Enter the value: ')
                movies.insert_at_begining(value)
            case 2:
                value = input('Enter the value')
                movies.insert_at_end(value)
            case 3:
                value = input('Enter the value: ')
                index = int(input('Enter the index: '))
                movies.insert_at_end(value, index)
            case 4:
                movies.remove_at_first()
            case 5:
                movies.remove_at_end()
            case 6:
                index = int(input('Enter the index: '))
                movies.remove_at_index(index)
            case 7:
                length = movies.get_length()
                print('Length is ' + length)

# movies.insert_at_begining('harry potter')
# movies.insert_at_begining('narnia')
# movies.insert_at_begining('evil dead')

# movies.insert_at_end('conjuring')
# movies.insert_at_end('grudge')

# movies.insert_at_index('insidious', 2)

# movies.remove_at_first()

# movies.remove_at_index(2)

# movies.remove_at_last()

# movies.print_elements()
