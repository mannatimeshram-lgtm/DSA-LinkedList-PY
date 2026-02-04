"""
1.create a LL 10 - 20 -30
2.transverse and print 
3.insert 5 at beginning 
4.insert 40 at end 
5.transverse again 
"""
class Node:
    def __init__(self, info , next=None ):
        self.info = info 
        self.next = next

class SLList:
    def __init__(self, head=None):
        self.head = head 

    def addInList(self , value):
        temp = Node(value)
        if (self.head != None ):
            t1 = self.head
            while (t1.next !=None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertInBeg(self , value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def printLL(self):
        t1 = self.head
        while (t1.next !=None):
            print(t1.info)
            t1 = t1.next
        print(t1.info)

LL = SLList( )
LL.addInList(10)
LL.addInList(20)
LL.addInList(30)
LL.addInList(40)
LL.insertInBeg(5)
LL.printLL()