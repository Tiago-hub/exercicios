class calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set_values(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        a = self.x + self.y
        return a
    
    def subtract(self):
        a = self.x - self.y
        return a
    

    def mul(self):
        a = self.x * self.y
        return a
    

    def div(self):      
        
        if (self.y == 0):
            a = "You can't divide by zero!"
        else:
            a = self.x / self.y  

        return a