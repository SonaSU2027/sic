class Node:
    def __init__(self, data=0):
        self.link = None
        self.data = data
        print(f'Node with data {data} created')

class Sll:
    def __init__(self):
        self.head = None
        print('An empty Sll is created')


    def add_at_pos(self):
        pos=int(input('Enter the position at which the node to be added'))
        data=int(input('enter the data to be added:')) 
        node = Node(data)          
        temp = self.head
        if pos == 0:
           
           
           self.head = node
           return
        else:
            for i in range(pos-1):
                if not temp:
                    print('Position out of bound')
                    return
                temp=temp.link
            node.link=temp.link
            temp.link=node 
       
    def delete_at_pos(self):
        pos=int(input('Enter the position at which the node to be deleted:'))
        temp = self.head
        if pos == 0:
            self.head=temp.link
            temp=None
            return    
        prev = None
        for i in range(pos):
            prev = temp
            temp = temp.link
            if not temp:
                print('position out of bound')
                return
        prev.link = temp.link
        temp = None


    def display_reverse(self, node):
        if node is None:
            return
        self.display_reverse(node.link)
        print(node.data, end=' ')

sll = Sll()
sll.add_at_pos()
sll.add_at_pos()
sll.add_at_pos()
sll.display_reverse(sll.head)
sll.delete_at_pos()
sll.display_reverse(sll.head)

