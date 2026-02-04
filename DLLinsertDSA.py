"""
1. create a DLL
2. insert an  element at the end. 
"""

class Node :
    def __init__(self , data = None):
        self.data = data
        self.next = None
        self.prev = None 

class DLlist:
    def __init__(self ):
        self.head =None

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
    
    def printDLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next 
        print(t1.data)


obj= DLlist()   
obj.ELEatEnd(10)
obj.ELEatEnd(20)
obj.ELEatEnd(30)
obj.ELEatEnd(40)
#adding element at the end of DLL aafter creating one 
obj.ELEatEnd(50)
obj.printDLL()


