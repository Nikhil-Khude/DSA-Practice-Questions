class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def append(self, value):
        temp = node(value)
        if self.head == None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

    # 2. Traverse and print node values
    def printll(self):
        t1 = self.head
        while t1 != None:
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")

  




  # 3. Insert node at specific position
    def insert(self, value, pos):
        temp = node(value)
        if pos == 1:
            temp.next = self.head
            self.head = temp
            return

        t1 = self.head
        for i in range(pos - 2):
            if t1 == None:
                print("Invalid position")
                return
            t1 = t1.next

        if t1 == None or pos < 1:
            print("Invalid position")
            return

        temp.next = t1.next
        t1.next = temp

    # 4. Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        if slow != None:
            print("Middle:", slow.data)
        else:
            print("List is empty")

   






 # 5. Delete node
    def delete(self, value):
        t1 = self.head

        if t1 != None and t1.data == value:
            self.head = t1.next
            return

        while t1 != None and t1.next != None:
            if t1.next.data == value:
                t1.next = t1.next.next
                return
            t1 = t1.next

        print("Value not found")

    # 6. Reverse list
    def reverse(self):
        prev = None
        t1 = self.head

        while t1 != None:
            nextnode = t1.next
            t1.next = prev
            prev = t1
            t1 = nextnode

        self.head = prev

    # 7. Sum of every two consecutive nodes
    def pairsum(self):
        t1 = self.head
        while t1 != None and t1.next != None:
            print(t1.data + t1.next.data)
            t1 = t1.next


s = SLL()

while True:
    print("\n1.Create  2.Traverse  3.Insert")
    print("4.Middle  5.Delete  6.Reverse  7.Pair Sum  8.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            value = int(input("Enter value: "))
            s.append(value)

    elif ch == 2:
        s.printll()

    elif ch == 3:
        value = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        s.insert(value, pos)

    elif ch == 4:
        s.middle()

    elif ch == 5:
        value = int(input("Enter value to delete: "))
        s.delete(value)

    elif ch == 6:
        s.reverse()
        print("List reversed")

    elif ch == 7:
        s.pairsum()

    elif ch == 8:
        break

    else:
        print("Invalid choice") 			 
