class intertest:
    def __init__(self):
        self.intervar1 = 5
        self.intervar2 = 6

class test:
    
    def __init__(self):
        self.var1 = 0
        self.var2 = 0
    
    def func(self, inter):
        return dir(inter) 

x = [1,2,3,4,5]

try: 
    print x[5]
except:
    pass


