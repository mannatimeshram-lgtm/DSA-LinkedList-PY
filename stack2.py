
class Node:
    def __init__(self , data):
        self.data= data
        self.next = None 

class Stack :
    def __init__(self):
        self.top = None

    def push(self, value):
        temp= Node(value)
        temp.next = self.top
        self.top = temp 
        print(value, "pushed ")

    def peek(self):
        if self.top is None :
            print("Stack is Empty")
            return None
        return self.top.data
    
    def pop(self):
        if self.top is None :
            print("Stack is Empty")
            return None
        removed = self.top.data
        self.top = self.top.next
        return removed
    
    def printS(self):
        t1 = self.top
        while t1 :
            print(t1.data , end = " -->")
            t1 = t1.next
        print("None")

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)

print(" Peek :" ,stk.peek())
print("Delete:" , stk.pop())
print("Delete:" , stk.pop())
         
         