import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Sll:
    def __init__(self):
        self.head = Node(None)
        print('Head node created')
        print('Enter 1.insert 2.delete 3.display in reverse order 4.exit.')

    def insert_at_pos(self):
        data = int(input('Enter the data to be inserted: '))
        pos = int(input('Enter the position to be inserted: '))
        new_node = Node(data)
        if pos == 0:
            new_node.link = self.head.link
            self.head.link = new_node
            return
        else:
            temp = self.head.link
            i = 1
            while i < pos:
                if temp is None:
                    print('Position out of bound')
                    return
                temp = temp.link
                i += 1
            if temp is None:
                print('Position out of bound')
                return
            new_node.link = temp.link
            temp.link = new_node

    def delete_at_pos(self):
        if self.head.link is not None:
            pos = int(input('Enter the position to be deleted: '))
            temp = self.head.link
            if pos == 0:
                self.head.link = temp.link
                print('Deleted node is:', temp.data)
                temp = None
                return
            else:
                i = 1
                prev = self.head
                while i <= pos:
                    if temp is None:
                        print('Position out of bound')
                        return
                    prev = temp
                    temp = temp.link
                    i += 1
                if temp is None:
                    print('Position out of bound')
                    return
                prev.link = temp.link
                print('Deleted node is:', temp.data)
                temp = None
        else:
            print('List is empty')

    def display_reverse(self, head):
        if head is None:
            return
        else:
            self.display_reverse(head.link)
            print(head.data)

    def match_user_choice(self, choice):
        match choice:
            case 1:
                self.insert_at_pos()
            case 2:
                self.delete_at_pos()
            case 3:
                self.display_reverse(self.head.link)
            case 4:
                print('Program ended')
                sys.exit()
            case _:
                print('Invalid choice')

sll = Sll()
while True:
    choice = int(input('Enter your choice: '))
    sll.match_user_choice(choice)
