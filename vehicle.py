class Vehicle:
    def __init__(self,make,model,color):
        self.make = make 
        self.model = model
        self.color = color 

    def move(self):
        print("starts moving")
    def hoot(self):
        print("starts hooting")

class Bus(Vehicle):
    def __init__(self,make,model,color,capacity):
      super().__init__(make,model,color)
      self.capacity = capacity
    
    def start_bording(self):
        print("the bus is now boarding")

class Lorry(Vehicle):
    def __init__(self,make,model,color,max_load):
        super().__init__(make,model,color)
        self.max_load = max_load
    def load(self):
        print("started loading")
  