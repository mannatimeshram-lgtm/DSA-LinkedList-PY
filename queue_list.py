class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)== 0 

    def insertion(self, value):
        self.items.append(value)
        return self.items 
    
    def deleteQ(self):
        if (self.isEmpty()):
            print(" Queue is Empty.")
        else:
            return self.items.pop(0)

obj = Queue()

# this value in insertion are getting save in memory .
obj.insertion(10)
obj.insertion(20)
obj.insertion(30)
obj.insertion(40)

print(obj.deleteQ())
print(obj.deleteQ())
print(obj.deleteQ())
print(obj.deleteQ())
print(obj.deleteQ())      # Till this deletion , queue will be empty.

