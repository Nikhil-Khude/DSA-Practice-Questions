

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class sll:
    def __init__(self, head=None):
        self.head = head

    # Insert node at the end
    def append(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

    # Insert node at a specific position
    def insert_position(self, value, pos):
        temp = Node(value)

        if pos == 1:
            temp.next = self.head
            self.head = temp
            return

        t1 = self.head
        count = 1

        while t1 != None and count < pos - 1:
            t1 = t1.next
            count += 1

        if t1 == None:
            print("Invalid position")
            return

        temp.next = t1.next
        t1.next = temp

    # Display linked list
    def display(self):
        t1 = self.head
        while t1 != None:
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")


# Main program
l1 = sll()

l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)

print("Before insertion:")
l1.display()

l1.insert_position(25, 3)

print("After insertion:")
l1.display()

