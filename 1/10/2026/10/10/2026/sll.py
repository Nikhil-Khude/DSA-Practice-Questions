def solution():
    class node:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next
    class sll:
        def __init__(self,head=None):
            self.head=head

        def append(self,value):
            temp=node(value)
            if(self.head !=None):
                t1=self.head
                while(t1.next !=None):
                    t1=t1.next
                t1.next=temp
            else:
                self.head=temp

        def beg(self,value):
            temp=node(value)
            t1=self.head
            temp.next=self.head
            self.head=temp

        def mid(self, value, x):
            temp = node(value)
            t1 = self.head
            while (t1.next!=None):
                if t1.data == x:
                    temp.next = t1.next
                    t1.next = temp
                    return
                t1 = t1.next

        def delt(self,value):
            t1=self.head
            prev=t1
            while(t1.next!=None):
                if(t1.next==value):
                    prev.next=t1.next
                else:
                    prev=t1
                    t1=t1.next
        def find(self):
            slow=self.head
            fast=self.head
            while(fast !=None and fast.next !=None):
                slow=slow.next
                fast=fast.next.next

            if slow !=None:
                print(slow.data)

        

                

        def printsll(self):
            t1=self.head
            while(t1.next!=None):
                print(t1.data,end=" ")
                t1=t1.next
            print(t1.data,end=" ")

        

    obj=sll()
    obj.append(10)
    obj.append(20)
    obj.append(30)
    obj.mid(40,20)
    obj.beg(50)
    obj.find()
    obj.delt(50)
    obj.printsll()
solution()