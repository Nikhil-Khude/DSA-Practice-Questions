

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class sll:
    def __init__(self, head=None):
        self.head = head

    # Q1. Create Linked List (append)
    def append(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

    # Q2. Traverse and print node values
    def traverse(self):
        t1 = self.head
        while t1 != None:
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")

    # Q3. Insert node at a specific position
    def insert(self, value, pos):
        temp = Node(value)

        if pos < 1:
            return

        if pos == 1:
            temp.next = self.head
            self.head = temp
        else:
            t1 = self.head

            for i in range(pos - 2):
                if t1 == None:
                    return
                t1 = t1.next

            if t1 == None:
                return

            temp.next = t1.next
            t1.next = temp

    # Q4. Delete node at a specific position
    def delete(self, pos):
        if self.head == None or pos < 1:
            return

        if pos == 1:
            self.head = self.head.next
        else:
            t1 = self.head

            for i in range(pos - 2):
                if t1 == None:
                    return
                t1 = t1.next

            if t1 == None or t1.next == None:
                return

            t1.next = t1.next.next

    # Print linked list
    def printll(self):
        t1 = self.head
        while t1 != None:
            print(t1.data, end=" ")
            t1 = t1.next
        print()


obj = sll()

obj.append(10)
obj.append(20)
obj.append(30)
obj.traverse()
obj.insert(15, 2)
obj.traverse()
obj.delete(2)
obj.traverse()


