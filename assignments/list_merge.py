class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def list_merge(self, list1, list2):
        """
        Checks if two linked lists merge at a certain node.

        Args:
            list1: The head of the first linked list.
            list2: The head of the second linked list.

        Returns:
            The position where the lists merge (1-based index), or None if they don't merge.
        """

        node1 = list1
        node2 = list2
        pos1 = 1
        pos2 = 1
        nodes_visited = set()

        while node1:
            nodes_visited.add(node1)
            node1 = node1.next
            
        node1 = list1
        while node2:
            if node2 in nodes_visited:
                # Find the position within the first list.
                node1 = list1
                position = 1
                while node1 is not node2:
                    node1 = node1.next
                    position +=1
                return position
            node2 = node2.next
            
        return None

    def display(self):
        """Prints the linked list to console"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()


list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

list2.append(6)
list2.append(7)


current = list1.head
while current.data != 4:
    current = current.next
merge_point = current

current = list2.head
while current.next:
    current = current.next

current.next = merge_point


# Check if the lists merge
merge_position = list3.list_merge(list1.head, list2.head)

if merge_position:
    print(f"The lists merge at position: {merge_position}")
else:
    print("The lists are not merged")

print("List1: ", end="")
list1.display()
print("List2: ", end="")
list2.display()