"""
1. create a DLL
2. insert an element at the beginning.
"""
class Node :
    def __init__(self , data = None):
        self.data = data
        self.next = None
        self.prev = None 

class DLlist:
    def __init__(self ):
        self.head =None

# TO INSERT AN ELEMENT AT THE END OF THE DOUBLY LINKED LIST..
    def ELEatEnd( self , value):
        temp = Node(value)
        
        #if no dll is already formed 
        if self.head == None :
            self.head = temp 
            return
       
        t1= self.head
        while (t1.next != None):
            t1 = t1.next 
        t1.next = temp 
        temp.prev = t1 
        return

# TO INSERT AN ELEMENT AT THE BEGINNING OF THE DOUBLY LINKED LIST..    
    def eleATBeg(self, value):
        temp = Node (value)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp 
    
    def printDLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data , end = " <--> ")
            t1 = t1.next 
        print(t1.data)

obj= DLlist()   
obj.ELEatEnd(10)
obj.ELEatEnd(20)
obj.ELEatEnd(30)
obj.ELEatEnd(40)
obj.ELEatEnd(50)
obj.eleATBeg(5)             # adding an element..
obj.printDLL()

