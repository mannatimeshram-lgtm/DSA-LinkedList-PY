class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def insertion(self , value):
        temp = Node (value)

        if self.front is None:
            self.front = temp
            self.rear= temp
        else:
            self.rear.next = temp
            self.rear = temp

    def deletion(self):
        if self.front is None:
            print("Qoueue is empty")
            return 
        
        print("Removed:", self.front.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None
       
obj  = QueueLL()
obj.insertion(10)
obj.insertion(20)
obj.insertion(30)
obj.insertion(40)

obj.deletion()
obj.deletion()
obj.deletion()