class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

class sll:
    def __init__(self,head=None):
        self.head= head

    def append(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

#Traverse and print the node values 

    def traverse(self):
        t1 = self.head

    while t1 != None:
        print(t1.data, end=" > ")
        t1 = t1.next

    print("None")

# Insert node at a specific position
    # At beg
    def insert(self, value, pos):
        temp = Node(value)

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

    def delete_alternate(self):
         t1 = self.head
     
         while t1 != None and t1.next != None:
             t1.next = t1.next.next
             t1 = t1.next  

    def printll(self):
        t1= self.head
        while t1.next!=None:
            print(t1.data,end=" ")
            t1=t1.next



obj=sll()
obj.append(10)
obj.append(20)
obj.traverse()
obj.append(30)
obj.printll()
